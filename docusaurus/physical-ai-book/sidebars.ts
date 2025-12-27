import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Manual sidebar configuration for the Physical AI & Humanoid Robotics book
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
        'module-2-digital-twin/chapter-1-simulation-environments',
        'module-2-digital-twin/chapter-2-physics-engines-modeling',
        'module-2-digital-twin/chapter-3-virtual-testing'
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      items: [
        'module-3-ai-robot-brain/index',
        'module-3-ai-robot-brain/chapter-1-perception-systems',
        'module-3-ai-robot-brain/chapter-2-planning-control',
        'module-3-ai-robot-brain/chapter-3-ai-integration'
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      items: [
        'module-4-vision-language-action/index',
        'module-4-vision-language-action/chapter-1-multimodal-ai',
        'module-4-vision-language-action/chapter-2-computer-vision',
        'module-4-vision-language-action/chapter-3-nlp',
        'module-4-vision-language-action/chapter-4-action-execution'
      ],
    },
    {
      type: 'category',
      label: 'Module 5: Capstone: Autonomous Humanoid',
      items: [
        'module-5-capstone/index',
        'module-5-capstone/chapter-1-system-integration',
        'module-5-capstone/chapter-2-humanoid-design',
        'module-5-capstone/chapter-3-autonomous-behaviors'
      ],
    },
  ],
};

export default sidebars;
