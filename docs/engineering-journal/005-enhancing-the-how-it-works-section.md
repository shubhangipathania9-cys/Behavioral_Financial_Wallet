# Smart Wallet Engineering Journal

## Entry #5 — Enhancing the "How It Works" Section and Understanding CSS Styling

**Date:** 24 July 2026

### Today's Goal

Improve the "How It Works" section by making it visually appealing while understanding the CSS concepts used behind the design.

### Work Completed Today

- Improved the "How It Works" section by giving each step card a unique visual identity.
- Added separate classes (`step-1`, `step-2`, `step-3`) to customize individual cards while keeping the common styling inside the `step-card` class.
- Applied different shades of green to the borders of each card to create a subtle sense of progression.
- Added matching colors to the step icons for better visual consistency.
- Fixed a layout issue caused by an incorrect HTML closing tag (`</>`), replacing it with the correct `</div>`.
- Refined the hover effect for the step cards using:
  - `transform: scale(1.02)`
  - `border-color`
  - `box-shadow`
- Reviewed and understood several important CSS properties and selectors.

### Concepts Learned

- Difference between `color` and `background-color`.
- Why a transparent border is useful before changing the border color on hover.
- Purpose of the `transition` property.
- How multiple classes work in HTML.
- Descendant selectors such as `.step-2 .step-icon`.
- Difference between translating an element and scaling an element.
- Importance of maintaining a consistent color palette for a professional UI.

### Current Progress

The landing page now includes:

- Hero Section
- Features Section
- How Smart Wallet Works Section

Each section now has its own visual identity while maintaining a consistent design language across the application.

### Reflection

Today's session focused more on understanding than simply writing code. I learned how CSS selectors, multiple classes, hover effects, transitions, and color hierarchy work together to create a clean and professional interface. I also realized that thoughtful use of colors can strengthen the product's story without making the design feel overwhelming.
