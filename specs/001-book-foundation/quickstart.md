# Quickstart Guide: Physical AI & Humanoid Robotics Book

## Overview
This guide will help you set up and run the Physical AI & Humanoid Robotics book locally.

## Prerequisites
- Node.js v20+ installed
- npm or yarn package manager
- Git

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Navigate to the Docusaurus project directory:
```bash
cd docusaurus
```

3. Install dependencies:
```bash
npm install
# or
yarn install
```

4. Start the development server:
```bash
npm run start
# or
yarn start
```

5. Open your browser to [http://localhost:3000](http://localhost:3000) to view the book.

## Project Structure
- `docs/` - Contains all the book content in MDX format
- `src/` - Custom React components and styles
- `static/` - Static assets like images
- `docusaurus.config.js` - Main Docusaurus configuration
- `sidebars.js` - Navigation sidebar configuration

## Adding Content
To add new content:
1. Create a new MDX file in the appropriate module directory in `docs/`
2. Add the new file to the sidebar configuration in `sidebars.js`
3. Ensure the content follows the established format and styling

## Building for Production
To build the static site for deployment:
```bash
npm run build
# or
yarn build
```

The built site will be in the `build/` directory and can be served by any static hosting service.

## Deployment
The site is configured for GitHub Pages deployment. After building, the `build/` directory can be deployed to GitHub Pages.