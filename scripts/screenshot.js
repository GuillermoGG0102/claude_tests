#!/usr/bin/env node

/**
 * Convert HTML infographic to PNG screenshot using Puppeteer
 * Usage: node scripts/screenshot.js
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function htmlToScreenshot() {
  const htmlFile = path.resolve('examples/claude-skills-linkedin-v3.html');
  const outputFile = path.resolve('examples/claude-skills-infographic.png');

  console.log('📸 Launching browser...');

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  try {
    const page = await browser.newPage();

    // Set viewport to 1080px (optimal for LinkedIn infographics)
    await page.setViewport({
      width: 1080,
      height: 1200,
      deviceScaleFactor: 2  // 2x for crisp quality
    });

    console.log('🌐 Loading HTML file...');
    await page.goto(`file://${htmlFile}`, { waitUntil: 'networkidle0' });

    // Get actual content height
    const height = await page.evaluate(() => {
      return document.documentElement.scrollHeight;
    });

    // Adjust viewport to actual content (keep 1080px wide)
    await page.setViewport({
      width: 1080,
      height: height,
      deviceScaleFactor: 2
    });

    console.log('📷 Taking screenshot...');
    await page.screenshot({
      path: outputFile,
      fullPage: true
    });

    console.log(`✅ PNG saved: ${outputFile}`);
    console.log(`📊 Dimensions: 1080 x ${height}px (2x quality)`);
    console.log('📤 Ready for LinkedIn!');

  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  } finally {
    await browser.close();
  }
}

// Install puppeteer if needed
async function ensurePuppeteer() {
  try {
    require('puppeteer');
  } catch (e) {
    console.log('📦 Installing puppeteer...');
    const { execSync } = require('child_process');
    execSync('npm install puppeteer', { stdio: 'inherit' });
  }
}

// Run
ensurePuppeteer().then(() => {
  htmlToScreenshot().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
  });
});
