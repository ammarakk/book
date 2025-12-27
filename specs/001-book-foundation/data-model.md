# Data Model: Phase 1 – Physical AI & Humanoid Robotics Book Foundation

## Overview
This document defines the data models for the Physical AI & Humanoid Robotics book foundation. Since this is a static content site, the "data" primarily consists of content structures and metadata.

## Content Entities

### Module
**Description**: A major section of the book that covers a specific topic area in Physical AI & Humanoid Robotics

**Fields**:
- id: String (unique identifier, e.g., "module-1", "module-2")
- title: String (e.g., "The Robotic Nervous System", "The Digital Twin")
- description: String (brief overview of the module content)
- order: Number (sequence number for navigation)
- chapters: Array<Chapter> (list of chapters in this module)
- heroImage: String (path to the hero image for this module)
- metadata: Object (SEO and other metadata)

**Validation**:
- id must be unique across all modules
- title must not be empty
- order must be a positive integer
- chapters must contain at least one chapter

### Chapter
**Description**: A subsection within a module that covers specific topics

**Fields**:
- id: String (unique identifier, e.g., "module-1-chapter-1")
- moduleId: String (reference to the parent module)
- title: String (chapter title)
- description: String (brief overview of the chapter content)
- order: Number (sequence within the module)
- sections: Array<Section> (list of sections in this chapter)
- content: String (path to the content file or inline content)
- heroImage: String (path to the hero image for this chapter, optional)
- metadata: Object (SEO and other metadata)

**Validation**:
- id must be unique across all chapters
- moduleId must reference an existing module
- title must not be empty
- order must be a positive integer
- content must exist and be valid

### Section
**Description**: A subsection within a chapter that covers specific concepts

**Fields**:
- id: String (unique identifier, e.g., "module-1-chapter-1-section-1")
- chapterId: String (reference to the parent chapter)
- title: String (section title)
- order: Number (sequence within the chapter)
- content: String (path to the content file or inline content)
- references: Array<Reference> (list of references in this section)
- metadata: Object (SEO and other metadata)

**Validation**:
- id must be unique across all sections
- chapterId must reference an existing chapter
- title must not be empty
- order must be a positive integer
- content must exist and be valid

### Reference/Citation
**Description**: A reference or citation to external sources and materials

**Fields**:
- id: String (unique identifier)
- title: String (title of the referenced material)
- url: String (URL to the referenced material)
- type: String (e.g., "book", "paper", "website", "video")
- description: String (brief description of the reference)
- sectionId: String (reference to the section containing this reference)

**Validation**:
- id must be unique across all references
- url must be a valid URL
- type must be one of the allowed values
- sectionId must reference an existing section

### Footer Content
**Description**: Information displayed in the footer including links and legal information

**Fields**:
- id: String (unique identifier, typically "footer")
- copyrightText: String (copyright information)
- links: Array<Object> (list of links with title and URL)
- legalInfo: String (legal disclaimers and information)
- contactInfo: String (contact information)

**Validation**:
- id must be "footer"
- copyrightText must not be empty
- links must have valid URLs

## Content File Structure

### MDX Content Files
The actual content will be stored in MDX files following this structure:

```
docs/
├── module-1-robotic-nervous-system/
│   ├── index.mdx
│   ├── chapter-1-ros2-architecture.mdx
│   ├── chapter-2-nodes-topics-services.mdx
│   └── chapter-3-practical-examples.mdx
├── module-2-digital-twin/
│   ├── index.mdx
│   └── ...
├── module-3-ai-robot-brain/
│   ├── index.mdx
│   └── ...
├── module-4-vision-language-action/
│   ├── index.mdx
│   └── ...
└── module-5-capstone/
    ├── index.mdx
    └── autonomous-humanoid.mdx
```

Each MDX file will contain frontmatter with metadata and the content in Markdown format with React components where needed.

## Theme and Styling Data

### Theme Configuration
The Neon robotic theme will be configured through the docusaurus.config.js file with the following key elements:

- Color palette (Neon colors: bright blues, cyans, purples against dark backgrounds)
- Typography (technical, clean fonts)
- Animation settings (subtle hover effects, transitions)
- Component styling (custom components for robotics diagrams, code examples)

## Navigation Data

### Sidebar Structure
The navigation will be defined in sidebars.js with the following structure:

```javascript
module.exports = {
  bookSidebar: [
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      items: [
        'module-1-robotic-nervous-system/index',
        'module-1-robotic-nervous-system/chapter-1-ros2-architecture',
        'module-1-robotic-nervous-system/chapter-2-nodes-topics-services',
        'module-1-robotic-nervous-system/chapter-3-practical-examples'
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      items: [
        'module-2-digital-twin/index',
        // ... more chapters
      ],
    },
    // ... more modules
  ],
};
```