UNIVERSAL FILTERS
1. Category

Placement: Very top of dashboard

CATEGORY

[ All ] [ Films (English) ] [ Films (Non-English) ]
        [ TV (English) ] [ TV (Non-English) ]

This is a single-select filter.

Default:

All

Everything on the dashboard responds to it.

This lets someone immediately switch from:

"What are Netflix's biggest titles?"

to:

"What does the English TV landscape look like?"

without needing multiple dashboards.

2. Date Range

Placement: Directly underneath Category, above KPIs.

Something like:

DATE RANGE
[ Jun 18, 2023 ───────────────────── Sep 27, 2026 ]

Default:

Entire available period

I think we should add this now.

It makes the dashboard considerably more useful because someone can ask:

What happened in 2023?
What happened in 2024?
How did 2025 compare?
What were the biggest titles over the last year?
Did a title have a huge peak but little longevity?

And importantly, it means every metric is answering the same question:

Within the selected category and time period...

That's much cleaner.

3. KPI ROW

Immediately underneath the universal filters.

Four cards:

┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────────────────┐
│   TITLES   │ │TOTAL VIEWS │ │TOTAL HOURS │ │ AVG TOTAL VIEWS /    │
│    2,712   │ │   20.4B    │ │   45.2B    │ │       TITLE          │
│            │ │            │ │            │ │       7.5M           │
└────────────┘ └────────────┘ └────────────┘ └──────────────────────┘
KPI 1 — Titles

Metric:

COUNTD(title)

Important: with category selected, this is distinct titles within the selected category and date range.

KPI 2 — Total Views
SUM(weekly_views)
KPI 3 — Total Hours Viewed
SUM(weekly_hours_viewed)
KPI 4 — Average Total Views per Title

This is:

SUM(weekly_views) / COUNTD(title)

We need to document this carefully.

It means:

Average accumulated reported views for titles appearing in the selected population during the selected period.

It does not mean average weekly views.

4. PRIMARY CHART — NETFLIX VIEWING OVER TIME

This should be the visual centerpiece.

Chart type

Line chart

Placement

Full-width underneath the KPI row.

┌───────────────────────────────────────────────────────────────┐
│ NETFLIX VIEWING OVER TIME                                     │
│                                                               │
│ Metric: [ Weekly Views ▼ ]                                    │
│                                                               │
│             ╭──────╮                                          │
│       ╭─────╯      ╰──────╮                                   │
│  ─────╯                    ╰────────────                      │
│                                                               │
│  Jun 2023      2024       2025       2026                     │
└───────────────────────────────────────────────────────────────┘
Metric

I would not show Views and Hours as two lines simultaneously.

They're too highly correlated and they're on very different scales.

Instead:

Subfilter / parameter

Viewing Metric

[ Weekly Views ▼ ]

Options:

Weekly Views
Weekly Hours Viewed

This gives the user two legitimate lenses without creating a visually messy dual-axis chart.

Calculation

Weekly Views:

SUM(weekly_views)

Weekly Hours:

SUM(weekly_hours_viewed)
X-axis

week

Granularity

Weekly.

That's important because the source data itself is weekly.

Interactivity

Clicking/hovering a point should show:

Week
Metric
Value

We can later decide whether clicking a period should filter the lower charts. I would not promise that interaction yet. First build the chart.

5. SECONDARY SECTION — TOP 10 TITLES

This is where the five validated ranking metrics come in.

Chart type

Horizontal bar chart

Placement

Under the timeline.

I'd give it roughly half the dashboard width.

┌─────────────────────────────────────┐
│ TOP 10 TITLES                       │
│ Rank Titles By: [ Total Views ▼ ]   │
│                                     │
│ KPop Demon Hunters █████████████    │
│ Squid Game S2      █████████        │
│ Stranger Things 5  ████████         │
│ Carry-On           ███████          │
│ ...                                 │
└─────────────────────────────────────┘
Subfilter

Rank Titles By

Options:

Total Views
Average Weekly Views
Peak Weekly Views
Total Hours Viewed
Weeks in Top 10
Number of titles

Fixed:

Top 10

I would not add a Top 5 / Top 10 / Top 20 selector yet.

Ten is enough to tell the story and keeps the chart clean.

Y-axis

Title

X-axis

Selected metric

Sort

Descending.

Category

Controlled by the universal Category filter.

Date

Controlled by the universal Date Range filter.

This is another reason I want the dashboard built primarily from global_clean.csv: changing the date range should dynamically change the rankings.

6. RIGHT SIDE — TITLE DETAIL

This is the piece I wouldn't build yet.

We have room conceptually for it:

┌─────────────────────┬─────────────────────┐
│                     │                     │
│    TOP 10 TITLES    │    TITLE DETAIL     │
│                     │                     │
│                     │                     │
└─────────────────────┴─────────────────────┘

But I don't want us inventing a chart just to fill the space.

Instead, after we build the first two charts, we can ask:

What question can't the dashboard answer yet?

Then build the detail visualization around that question.

That is much better portfolio practice than "dashboard needs three charts."

7. Proposed final dashboard layout

So the current locked blueprint is:

┌───────────────────────────────────────────────────────────────┐
│                    NETFLIX POPULARITY EXPLORER                │
│                                                               │
│ CATEGORY                                                       │
│ [ALL] [FILMS EN] [FILMS NON-EN] [TV EN] [TV NON-EN]          │
│                                                               │
│ DATE RANGE                                                    │
│ [ Jun 18 2023 ───────────────────────────── Sep 27 2026 ]    │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│ [ TITLES ] [ TOTAL VIEWS ] [ TOTAL HOURS ] [ AVG VIEWS/TITLE]│
│                                                               │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│                    NETFLIX VIEWING OVER TIME                  │
│                                                               │
│                    Metric: [Weekly Views ▼]                   │
│                                                               │
│                         LINE CHART                            │
│                                                               │
├───────────────────────────────────┬───────────────────────────┤
│                                   │                           │
│          TOP 10 TITLES             │       TITLE DETAIL       │
│                                   │                           │
│ Rank by: [Total Views ▼]          │       TBD                │
│                                   │                           │
│ Horizontal bar chart              │                           │
│                                   │                           │
└───────────────────────────────────┴───────────────────────────┘

The Title Detail area is deliberately TBD rather than forcing a weak visualization.

8. Filter architecture

Here's the important part:

Filter	Type	Scope	Purpose
Category	Universal filter	Entire dashboard	English/non-English + Film/TV
Date Range	Universal filter	Entire dashboard	Analyze different periods
Viewing Metric	Parameter	Timeline only	Views vs hours
Rank Titles By	Parameter	Top 10 only	Five ranking perspectives