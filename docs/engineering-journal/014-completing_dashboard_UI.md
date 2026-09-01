## Completing and Refining the Smart Wallet Dashboard UI\*\*

**Engineering Journal - Entry 014**

**Date:** 1 September 2026

### Today's Goal

Continue developing the Smart Wallet dashboard by completing its main frontend sections, refining the user interface, and deciding how different features should be organized across the application.

The main focus was to make the dashboard function as a clean overview of the user's financial activity rather than placing every feature and piece of information on a single page.

### What I Learned

- Learned how a dashboard should provide a high-level overview instead of displaying every detail of an application.

- Designed the Financial Overview section to display Total Balance, Available Money, Locked Savings, and Active Locks.

- Learned how Quick Actions can provide direct access to important wallet functions.

- Finalized the Quick Actions as Add Money, Create Lock, and Pay Now.

- Understood that payment functionality is important because it allows changes in the available balance to be represented meaningfully.

- Learned how static placeholder data can be used during frontend development before connecting the interface to the backend.

- Implemented a Money Locks Preview section containing the lock name, saved amount, goal amount, progress percentage, progress bar, and lock status.

- Learned how CSS Grid can be used to create responsive layouts for Money Lock cards.

- Added hover effects to dashboard cards to improve the visual feedback of interactive elements.

- Improved the visual hierarchy of financial values by using the Smart Wallet emerald green as the primary highlight color.

- Learned the importance of avoiding unnecessary information on the main dashboard.

- Decided that detailed Recent Activity should be moved to a separate History page.

- Planned separate pages for Money Locks, Payments, History, and future Insights functionality.

- Understood that separating features into dedicated pages will make Smart Wallet easier to navigate and expand as the project grows.

### Challenges Faced

One of the main design decisions during today's development was deciding whether Recent Activity and Smart Insights should be displayed directly on the dashboard.

Initially, the dashboard contained sections for Money Locks, Recent Activity, and Smart Insights. However, this started making the dashboard too large and caused too much information to appear on a single page.

I decided that the dashboard should primarily act as an overview page. Detailed transaction information will instead be placed on a separate History page, while complete Money Lock management will be handled through a dedicated Money Locks page.

Another small issue was the payment action description. The original wording described the feature as a "hypothetical payment." Since the user interface is intended to feel like a functional wallet while the backend is being developed as a simulation, I changed the description to focus on the actual user action: making a payment from the available balance.

I also reviewed the CSS and identified duplicate rules for the `main` element and `.overview-card p`. These were cleaned up to keep the stylesheet more organized and avoid unnecessary overriding of styles.

### Key Takeaways

- A dashboard should provide a concise overview rather than contain every application feature.

- Detailed information can be placed on dedicated pages to improve usability.

- Static data is useful for designing and testing frontend interfaces before backend integration.

- Money Locks are the central feature of Smart Wallet and should remain visible from the dashboard through a preview.

- Payment functionality is important because it allows wallet balances and transaction history to represent meaningful changes.

- CSS Grid can be used to create flexible layouts for dashboard components.

- Consistent colors, spacing, shadows, and hover effects improve the overall visual hierarchy of an application.

- Duplicate CSS rules should be removed to keep the stylesheet maintainable.

- Application architecture should be considered during frontend development rather than adding features to a single page without structure.

### Progress Made

- ✅ Completed the Smart Wallet dashboard header.

- ✅ Completed the personalized welcome section.

- ✅ Completed the Financial Overview section.

- ✅ Added Total Balance.

- ✅ Added Available Money.

- ✅ Added Locked Savings.

- ✅ Added Active Locks.

- ✅ Finalized the Quick Actions section.

- ✅ Added Add Money action.

- ✅ Added Create Lock action.

- ✅ Added Pay Now action.

- ✅ Completed the Money Locks Preview section.

- ✅ Added sample Money Lock cards.

- ✅ Added progress bars for Money Lock goals.

- ✅ Added lock status indicators.

- ✅ Added hover effects to dashboard cards.

- ✅ Refined dashboard spacing and section separation.

- ✅ Reviewed and cleaned duplicate CSS rules.

- ✅ Decided to move detailed Recent Activity to a separate History page.

- ✅ Planned a separate Money Locks page.

- ✅ Planned a separate Payments page.

- ⬜ Build the complete Money Locks page.

- ⬜ Build the Payments page.

- ⬜ Build the History page.

- ⬜ Connect dashboard values to the SQLite database.

- ⬜ Replace static dashboard data with real user data.

### Reflection

Today's session focused not only on building the Smart Wallet interface but also on thinking about the application's overall structure.

The most important design decision was realizing that the dashboard does not need to contain every feature. Its purpose is to give the user a quick understanding of their current financial situation and provide easy access to important actions.

The Money Locks Preview allows users to see their savings goals without overwhelming the dashboard with detailed information. Detailed transactions will instead be available through the History page, while Money Locks and Payments will have their own dedicated interfaces.

I also learned that frontend development can begin with static placeholder data. This allowed the layout and visual design to be tested before the database functionality is implemented. Later, these placeholders will be replaced with real values retrieved through Flask and SQLite.

With the main dashboard UI now complete, the next stage of development will be to build the dedicated Money Locks page and eventually connect it to the backend so that users can create, manage, and track their actual savings locks.
