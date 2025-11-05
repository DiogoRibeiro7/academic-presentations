# Capstone Projects Enhancement Guide

## Overview

This enhancement module provides **comprehensive materials** for semester-long capstone projects in data science courses. The module includes presentation slides, prerequisites materials, and competency tracking frameworks.

### Core Files

**1. Main Presentation (30 slides):** `capstone_projects_enhancements.tex`
- Project Framework Overview (2 slides + 2 knowledge check slides)
- Real-World Datasets by Domain (5 slides + 2 knowledge check slides)
- Progressive Milestones with Rubrics (4 slides + 3 knowledge check slides)
- Peer Review Components (3 slides + 2 knowledge check slides)
- Industry Mentor Connections (3 slides + 1 knowledge check slide)
- Project Templates and Examples (3 slides + 2 knowledge check slides)

**2. Prerequisites Appendix (8 slides):** `capstone_prerequisites_appendix.tex`
- Prerequisites Overview and Self-Assessment
- Learning Paths by Background (Software Eng, Stats/Math, Domain Expert)
- 8-Week Pre-Capstone Preparation Plan
- Just-in-Time Learning Strategy
- Growth Mindset and Getting Help
- Time Management for Success

**3. Competency Matrices:** `COMPETENCY_MATRICES.md`
- 7 detailed skill matrices (Programming, ML, Statistics, Software Engineering, Communication, Collaboration, Research)
- 4-level proficiency framework (Beginner → Expert)
- Milestone-specific competency requirements
- Self-assessment worksheets with tracking
- Portfolio development guidance

**4. Bibliography:** `bibliographies/capstone_projects_references.bib`
- 50+ references for datasets, methods, tools, and best practices

**Knowledge Check Features:**
- **Multiple Choice Questions** with detailed explanations
- **Conceptual Problems** requiring written responses (200-300 words)
- **Coding Challenges** with auto-grader specifications

---

## Integration Points

### Recommended Integration by Course Type

#### 1. **Statistical Learning Course**
**Best integration point:** After "Applications and Case Studies" section
**Slides to include:** All 30 slides
**Rationale:** Capstone projects are a natural extension of applied statistical learning, allowing students to implement methods learned in class on real datasets.

**Integration instructions:**
```latex
% In statistical_learning_beamer.tex
% After the "Applications and Case Studies" section

\input{statistical_learning_enhancements.tex}  % Existing enhancements
\input{capstone_projects_enhancements.tex}     % NEW: Capstone projects
```

#### 2. **Industry Focus / MLOps Course**
**Best integration point:** After "Business Stakeholder Communication" section or as final section
**Slides to include:** All slides, with emphasis on Milestones 4, Industry Mentors, and Templates
**Rationale:** Capstone projects emphasize production-ready code and industry practices.

**Integration instructions:**
```latex
% In industry_focus_beamer.tex or similar
% After MLOps/deployment content

\input{capstone_projects_enhancements.tex}
```

#### 3. **Causal Inference Course**
**Best integration point:** After "Practical Applications and Case Studies"
**Slides to include:**
- Project Framework (all)
- Domain 1 (Healthcare), Domain 3 (Social Impact) - focus on causal projects
- All milestone slides (emphasize causal methods in M3)
- Peer Review and Mentors (all)
- Templates (all)

**Selective integration:**
```latex
% In causal_inference_beamer.tex
% After applications section

% Include only specific sections from capstone_projects_enhancements.tex
% See "Selective Integration" section below for details
```

#### 4. **Feature Engineering Course**
**Best integration point:** After "Practical Considerations and Best Practices"
**Slides to include:** Focus on Milestone 2 (feature engineering pipeline) and data quality sections
**Rationale:** Demonstrates end-to-end feature engineering on messy real-world data.

#### 5. **Standalone Capstone Workshop**
**Best use:** First week of semester orientation
**Slides to include:** All 30 slides
**Rationale:** Dedicated session to introduce capstone requirements, set expectations, and connect students with mentors.

---

## Full Integration Instructions

### Method 1: Complete Integration (Recommended)

To integrate all capstone project slides into your presentation:

```latex
% In your main .tex file (e.g., statistical_learning_beamer.tex)
% At the desired integration point:

\input{capstone_projects_enhancements.tex}
```

**Result:** Adds all 30 slides as a new section titled "Semester-Long Capstone Projects"

**LaTeX structure:**
- The file creates a new `\section{Semester-Long Capstone Projects}`
- Subsections for each major topic
- Knowledge check frames interspersed after content
- Uses consistent color scheme with your existing slides

### Method 2: Selective Integration

To include only specific sections, you'll need to copy relevant frames from `capstone_projects_enhancements.tex` into your main file.

**Example: Include only Project Framework and Milestones**

```latex
% In your main .tex file:

% -------------------- From capstone_projects_enhancements.tex --------------------
% Copy frames from lines 20-250 (Project Framework)
% Copy frames from lines 400-650 (Milestones)
% ---------------------------------------------------------------------------------
```

**Sections and their line ranges** (approximate):
- **Section 1: Project Framework** (lines 20-250)
  - Why Capstone Projects?
  - Semester Timeline
  - Knowledge Check 1

- **Section 2: Real-World Datasets** (lines 260-520)
  - Healthcare
  - Finance & E-commerce
  - Social Impact
  - Technology & Manufacturing
  - Dataset Access & Ethics
  - Knowledge Check 2

- **Section 3: Milestones** (lines 530-850)
  - Milestone 1-4 slides
  - Knowledge Check 3

- **Section 4: Peer Review** (lines 860-1050)
  - Why Peer Review
  - Review Template
  - Collaboration Skills
  - Knowledge Check 4

- **Section 5: Industry Mentors** (lines 1060-1250)
  - Mentor Matching
  - Touchpoint Schedule
  - Industry Presentations
  - Knowledge Check 5

- **Section 6: Templates** (lines 1260-1450)
  - Project Proposal Template
  - Documentation Standards
  - Example Projects
  - Resources
  - Knowledge Check 6

---

## Customization Options

### 1. Adjusting Timeline

The default timeline is **14 weeks**. To adjust for your semester length:

**Find and replace:**
```latex
% Line ~65: Semester Timeline table
% Modify the "Weeks" column to match your schedule

% Example for 12-week semester:
1-2 & M1: Discovery & ... & 15\% \\
3-5 & M2: Foundation & ... & 20\% \\
6-9 & M3: Advanced & ... & 25\% \\
10-11 & M4: Deployment & ... & 30\% \\
12 & Final & ... & 10\% \\
```

### 2. Modifying Grading Weights

To change the milestone weights (currently 15%, 20%, 25%, 30%, 10%):

**Edit the timeline table** (line ~65) and **rubric tables** for each milestone (lines ~300, 400, 500, 600)

### 3. Adding Your Own Datasets

To include institution-specific datasets:

**Edit Section 2** (Real-World Datasets):
```latex
% Add after line ~280 (or replace existing domains)

\begin{frame}{Domain X: Your Custom Domain}
\textbf{Description}

\begin{columns}
\begin{column}{0.5\textwidth}
\textbf{Available Datasets:}
% Your datasets here
\end{column}
\begin{column}{0.5\textwidth}
\textbf{Sample Project Ideas:}
% Your project ideas here
\end{column}
\end{columns}
\end{frame}
```

### 4. Customizing Knowledge Checks

Each knowledge check includes:
- Multiple choice questions (with `\pause` for progressive reveal)
- Conceptual problems (written responses)
- Coding challenges (with auto-grader specs)

**To modify:**
```latex
% Find the relevant Knowledge Check frame (search for "Knowledge Check")
% Edit questions, answers, or explanations as needed
% Maintain the \pause commands for reveal structure
```

**To disable knowledge checks entirely:**
```latex
% Comment out all frames with "Knowledge Check" in the title
% Lines: ~250, ~520, ~850, ~1050, ~1250, ~1450
```

### 5. Adding Your Institution's Resources

**Edit the "Additional Resources" frame** (line ~1350):
```latex
\begin{frame}{Additional Resources}
% Add your institution's:
% - Computing cluster access
% - Dataset repositories
% - Office hours schedule
% - Course Slack/Discord links
\end{frame}
```

---

## Bibliography Integration

The capstone projects module references the following sources that should be added to your bibliography:

**Required bibliography file:** `capstone_projects_references.bib`

**In your main .tex file preamble:**
```latex
\usepackage[backend=biber, style=authoryear]{biblatex}
\addbibresource{bibliographies/capstone_projects_references.bib}
```

**Key citations used:**
- `\cite{johnson2016mimic}` - MIMIC-III database
- `\cite{lendingclub}` - Lending Club dataset
- `\cite{mitchell2019model}` - Model Cards paper

---

## Knowledge Check Implementation Guide

### Auto-Grader Integration

The coding challenges include specifications for auto-graders. To implement:

#### Option 1: Manual Grading
- Students submit code to course platform (Canvas, Gradescope, etc.)
- TAs run test cases manually
- Provide feedback on edge cases

#### Option 2: Automated Testing (Recommended)
- Use **Gradescope Autograder** or similar platform
- Create test suites based on specifications in slides
- Students receive immediate feedback

**Example auto-grader setup (Python):**
```python
# For Knowledge Check 2: Disparate Impact function

import unittest
import numpy as np
from student_code import disparate_impact

class TestDisparateImpact(unittest.TestCase):
    def test_no_disparity(self):
        predictions = np.array([1,1,0,0,1,1,0,0])
        protected_attr = np.array([0,0,0,0,1,1,1,1])
        result = disparate_impact(predictions, protected_attr,
                                  protected_value=1, reference_value=0)
        self.assertEqual(result['di_ratio'], 1.0)
        self.assertTrue(result['passes_80_rule'])

    def test_adverse_impact(self):
        predictions = np.array([1,1,1,1,0,0,1,0])
        protected_attr = np.array([0,0,0,0,1,1,1,1])
        result = disparate_impact(predictions, protected_attr,
                                  protected_value=1, reference_value=0)
        self.assertEqual(result['di_ratio'], 0.25)
        self.assertFalse(result['passes_80_rule'])
```

#### Option 3: Notebook-Based Assessment
- Provide Jupyter notebooks with hidden test cells
- Use **nbgrader** for automated grading
- Students complete code cells, tests run automatically

### Written Response Grading

For conceptual problems (short answer questions):

**Grading rubric template:**
```
Knowledge Check X - Conceptual Problem

Criteria:
1. Understanding (40 points)
   - Demonstrates correct understanding of core concepts
   - Identifies key issues/trade-offs

2. Technical Accuracy (30 points)
   - Correct terminology and methods
   - Accurate descriptions

3. Clarity (20 points)
   - Well-organized response
   - Clear explanations

4. Completeness (10 points)
   - Addresses all parts of question
   - Within word limit

Total: 100 points
```

---

## Assessment Integration

### Using Knowledge Checks for Grading

You can use knowledge checks in several ways:

#### 1. **Formative Assessment (Recommended)**
- Not graded, used for self-assessment
- Discuss answers in class
- Encourage students to attempt before seeing solutions
- Use `\pause` commands to reveal answers progressively in lecture

#### 2. **Low-Stakes Quizzes**
- Each knowledge check = 1 quiz (6 total)
- Worth 1-2% of final grade each
- Students submit within 24 hours of lecture
- Auto-graded MCQs + manual review of written responses

#### 3. **Milestone Pre-Checks**
- Knowledge Checks 1-2: Required before M1 submission
- Knowledge Check 3: Required before M2/M3 submission
- Knowledge Checks 4-5: Required before M4 submission
- Knowledge Check 6: Required before final presentation
- Pass/fail (must score ≥70% to submit milestone)

#### 4. **In-Class Active Learning**
- Use MCQs with audience response system (PollEverywhere, Mentimeter)
- Students vote on answers
- Discuss common misconceptions
- Peer instruction methodology

---

## Lecture Timing Recommendations

### Full Module Delivery

If presenting all 30 slides as dedicated lectures:

**Session 1: Project Introduction (60 minutes)**
- Section 1: Project Framework (15 min)
- Knowledge Check 1 (10 min)
- Section 2: Real-World Datasets (25 min)
- Knowledge Check 2 (10 min)

**Session 2: Milestones Deep Dive (60 minutes)**
- Section 3: All Milestone slides (35 min)
- Knowledge Check 3 (25 min including coding challenge discussion)

**Session 3: Collaboration & Mentorship (60 minutes)**
- Section 4: Peer Review (20 min)
- Knowledge Check 4 (10 min)
- Section 5: Industry Mentors (20 min)
- Knowledge Check 5 (10 min)

**Session 4: Templates & Final Assessment (45 minutes)**
- Section 6: Templates and Resources (20 min)
- Knowledge Check 6 (25 min - comprehensive scenario)

### Compressed Delivery (Single Session)

For a 90-minute workshop covering highlights only:

**Minutes 0-15:** Project Framework Overview
- Why capstone projects (5 min)
- Semester timeline (10 min)

**Minutes 15-35:** Datasets and Domains
- Quick tour of 4 domains (15 min)
- Ethics checklist (5 min)

**Minutes 35-50:** Milestone Overview
- Walkthrough of M1-M4 expectations (15 min)

**Minutes 50-65:** Peer Review and Mentors
- Peer review process (7 min)
- Mentor touchpoints (8 min)

**Minutes 65-80:** Templates and Example
- Proposal template (5 min)
- Example project walkthrough (10 min)

**Minutes 80-90:** Q&A and Resources
- Questions (10 min)

---

## Student Handouts

Consider creating supplementary materials:

### 1. **Capstone Project Handbook (PDF)**
Export key slides as PDF handout:
```bash
# Using beamer handout mode
\documentclass[handout]{beamer}
```

Include:
- Timeline and rubrics
- Proposal template
- Review checklist
- Resources list

### 2. **Templates Repository**
Create a GitHub repo with:
```
capstone-templates/
├── project_proposal_template.md
├── milestone_checklist.md
├── peer_review_template.md
├── model_card_template.md
├── cookiecutter-project-template/
└── README.md
```

### 3. **Coding Challenge Starters**
Provide starter code for each coding challenge:
```
coding-challenges/
├── disparate_impact_starter.py
├── temporal_cv_starter.py
└── tests/
    ├── test_disparate_impact.py
    └── test_temporal_cv.py
```

---

## Troubleshooting

### Common LaTeX Issues

**Problem:** TikZ graphics not rendering
**Solution:** Ensure you have these packages in your preamble:
```latex
\usepackage{tikz}
\usetikzlibrary{shapes, arrows, positioning}
```

**Problem:** Bibliography not appearing
**Solution:** Make sure you compile with biber:
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

**Problem:** Colors not matching existing slides
**Solution:** Check your color definitions match. The enhancement uses:
```latex
\definecolor{navyblue}{RGB}{0, 51, 102}
\definecolor{forest}{RGB}{34, 139, 34}
\definecolor{crimson}{RGB}{220, 20, 60}
\definecolor{purple}{RGB}{128, 0, 128}
\definecolor{gold}{RGB}{255, 215, 0}
```

### Content Customization Issues

**Problem:** Timeline doesn't fit my semester
**Solution:** See "Adjusting Timeline" in Customization Options

**Problem:** Datasets are outdated
**Solution:** See "Adding Your Own Datasets" in Customization Options

**Problem:** Too many slides for my lecture time
**Solution:** Use "Compressed Delivery" guide or selective integration

---

## Feedback and Iteration

After first use, consider:

1. **Student feedback survey:**
   - Were knowledge checks helpful?
   - Was the timeline realistic?
   - What resources were most useful?

2. **Track milestone success:**
   - What percentage met each milestone deadline?
   - Common issues at each stage?
   - Where do students struggle most?

3. **Update content annually:**
   - New datasets and tools
   - Updated industry practices
   - Refined rubrics based on experience

---

## Prerequisites and Preparation Materials

### Using the Prerequisites Appendix

The `capstone_prerequisites_appendix.tex` file contains 8 slides designed to help students assess readiness and prepare for the capstone.

**When to use:**
- **Week 0 / Pre-semester:** Share with registered students before course starts
- **First class:** Present to set expectations
- **Prerequisite screening:** Help students self-select or prepare

**Integration options:**

#### Option 1: Pre-Capstone Orientation (Recommended)
Present before the main capstone slides as a "Week 0" session:
```latex
% Create a standalone prerequisites presentation
\documentclass[aspectratio=169]{beamer}
% ... your theme setup ...

\input{capstone_prerequisites_appendix.tex}
```

#### Option 2: Integrated into Main Presentation
Add at the beginning of the main capstone slides:
```latex
% In your main presentation, before capstone_projects_enhancements.tex
\input{capstone_prerequisites_appendix.tex}
\input{capstone_projects_enhancements.tex}
```

#### Option 3: Self-Study Materials
Export slides as PDF handout and share via course website for self-assessment.

### Prerequisites Content Breakdown

**Slide 1: Prerequisites Overview**
- Technical prerequisites (Python, Math, ML, Statistics)
- Conceptual prerequisites (Data science workflow)
- Soft skills (Communication, time management)
- Use for: Setting expectations, prerequisite enforcement

**Slide 2: Self-Assessment Checklist**
- 24 checkpoint questions across 5 categories
- Students check what they can do
- Scoring: 16-20 ready | 11-15 review gaps | <10 need prep
- Use for: Student self-assessment, identifying gaps

**Slide 3: Learning Paths by Background**
- Path 1: Software Engineer → Data Science
- Path 2: Statistics/Math → Data Science
- Path 3: Domain Expert → Data Science
- Each path includes 4-6 week preparation timeline
- Use for: Personalized preparation recommendations

**Slide 4: 8-Week Pre-Capstone Preparation Plan**
- Week-by-week curriculum for students with gaps
- Activities, assessments, and time commitments
- Final project to validate readiness
- Use for: Summer prep program, prerequisite course

**Slide 5: Just-in-Time Learning**
- You don't need to know everything upfront!
- Skills needed by each milestone
- Resources for learning during capstone
- Use for: Reducing anxiety, encouraging growth mindset

**Slide 6: Growth Mindset**
- Fixed vs. growth mindset examples
- Common capstone challenges and responses
- Strategies for success
- Use for: Setting positive tone, encouraging resilience

**Slide 7: Getting Help**
- 30-minute rule (try self, then ask)
- Where to ask (Slack, office hours, peers)
- How to ask good questions (template provided)
- Use for: Teaching help-seeking skills

**Slide 8: Time Management**
- Expected weekly time investment (13-20 hrs)
- Sample weekly schedule
- Avoiding burnout strategies
- Use for: Setting realistic expectations

### Customizing Prerequisites

**Adjusting difficulty:**
- **More rigorous:** Increase self-assessment pass threshold to 18+
- **More accessible:** Add "learning path 4" for complete beginners (12-week prep)
- **Domain-specific:** Add domain prerequisites (e.g., biology for health projects)

**Institution-specific:**
```latex
% Edit slide 1 to add your required courses
\textbf{Required Courses at [Your University]:}
\begin{itemize}
\item CS 101: Intro to Programming
\item STAT 201: Statistical Inference
\item DS 301: Machine Learning Fundamentals
\end{itemize}
```

---

## Competency Matrices Guide

### Using COMPETENCY_MATRICES.md

This comprehensive document helps students track skill development throughout the capstone.

**File format:** Markdown (easy to edit, share, and convert)
**Length:** ~6000 words, 7 matrices, multiple tracking worksheets
**Best for:** Student self-assessment, instructor evaluation, portfolio development

### Distribution Options

#### Option 1: Course Website (Recommended)
- Upload markdown file to course website
- Students download and fill out electronically
- Convert to PDF for easy sharing:
  ```bash
  pandoc COMPETENCY_MATRICES.md -o COMPETENCY_MATRICES.pdf
  ```

#### Option 2: Google Docs
- Convert to Google Doc
- Students make a copy for themselves
- Enables easy sharing with mentors/instructors

#### Option 3: Gradebook Integration
- Extract competency requirements into LMS gradebook
- Track student progress against milestone competencies
- Generate reports on class-wide skill development

### Competency Framework Overview

**4-Level Proficiency Scale:**
- **Level 1 (Beginner):** Limited experience, needs guidance
- **Level 2 (Intermediate):** Functional competence, independent on standard tasks
- **Level 3 (Advanced):** Strong proficiency, handles complex scenarios
- **Level 4 (Expert):** Mastery level, can teach and innovate

**Capstone Expectations:**
- **Start:** Level 2 in core areas (Python, ML, Stats)
- **M4 (Week 13):** Level 3 in project-specific areas
- **Stretch:** Level 4 in 1-2 specialization areas

### The 7 Competency Matrices

**Matrix 1: Technical Skills - Programming & Data Manipulation**
- Skills: Python, Pandas, NumPy, Data Viz, Debugging
- Critical for: All milestones, foundational

**Matrix 2: Technical Skills - Machine Learning**
- Skills: Supervised Learning, Model Evaluation, Feature Engineering, Hyperparameter Tuning, Interpretation, Ensembles, Deep Learning, Causal Inference
- Critical for: M2 (baseline), M3 (advanced methods)

**Matrix 3: Technical Skills - Statistics & Mathematics**
- Skills: Descriptive Stats, Probability, Hypothesis Testing, CIs, Regression, Experimental Design, Bayesian
- Critical for: M1 (EDA), M3 (validation)

**Matrix 4: Software Engineering & MLOps**
- Skills: Git, Code Organization, Testing, Documentation, API Development, Containerization, CI/CD, Deployment, Monitoring, Data Versioning
- Critical for: M4 (production readiness)

**Matrix 5: Communication Skills**
- Skills: Technical Writing, Data Viz, Presentations, Storytelling, Audience Adaptation, Code Communication
- Critical for: All milestones, especially M4 and final presentation

**Matrix 6: Collaboration & Professional Skills**
- Skills: Peer Review, Receiving Feedback, Project Management, Time Management, Problem Solving, Learning Agility, Ethics, Domain Knowledge
- Critical for: Ongoing throughout, peer review phases

**Matrix 7: Research Skills**
- Skills: Literature Review, Reading Papers, Experimental Design, Result Interpretation, Reproducibility, Scientific Writing
- Critical for: M3 (applying methods from papers), M4 (technical report)

### Implementation Strategies

#### Strategy 1: Milestone-Based Assessment
**Use milestone-specific competency requirements from the document.**

At each milestone submission:
1. Student self-assesses against required competencies
2. Instructor evaluates student's demonstrated level
3. Gap analysis identifies areas for improvement
4. Feedback references specific competency levels

**Example M2 feedback:**
> "Your feature engineering shows strong Level 3 competency - systematic approach with domain-specific features. However, code organization is still at Level 1 - consider refactoring into modules (see Matrix 4, Code Organization L2 criteria)."

#### Strategy 2: SMART Goals Integration
**Students set competency-based learning goals.**

At the start of each milestone:
1. Student reviews upcoming competency requirements
2. Sets 2-3 SMART goals for skill development
3. Documents in milestone proposal
4. Reflects on achievement in milestone report

**Template included in COMPETENCY_MATRICES.md**

#### Strategy 3: Portfolio Development
**Map competencies to resume/portfolio items.**

End of capstone:
1. Student identifies all Level 3+ competencies
2. For each, creates portfolio demonstration
3. Prepares competency-based resume bullets
4. Practices explaining competencies in interviews

**Guidance and examples included in document**

### Weekly Tracking Workflow

**Week 0:** Initial self-assessment
- Students fill out all 7 matrices
- Identify gaps vs. minimum requirements
- Set learning goals

**Weekly:** Quick check-in
- Did I use this skill this week?
- Did my proficiency increase?
- What's blocking improvement?

**Week 7:** Mid-semester formal reassessment
- Re-evaluate all competencies
- Calculate growth
- Adjust goals for second half

**Week 14:** Final assessment
- Complete final evaluation
- Calculate total growth
- Portfolio planning

### Grading with Competency Matrices

**Option A: Rubric Alignment**
Map rubric criteria to competency levels:
- "Excellent" (90-100%) = Level 3-4
- "Good" (80-89%) = Level 2-3
- "Satisfactory" (70-79%) = Level 2
- "Needs Improvement" (<70%) = Level 1

**Option B: Competency-Based Grading**
Each milestone requires demonstrated competencies:
- M1: Achieve L2 in 5 core competencies (50 pts each)
- M2: Achieve L2 in 8 competencies (30 pts each)
- M3: Achieve L3 in 5 advanced competencies (50 pts each)
- M4: Achieve L3 in 7 production competencies (35 pts each)

**Option C: Growth-Based Bonus**
Base grade on deliverables; bonus for competency growth:
- +5% for 10+ competencies improved by 1 level
- +10% for 5+ competencies improved by 2 levels
- +15% for exceptional growth (L1→L3 in critical area)

### Customizing Competency Matrices

**Add institution-specific skills:**
```markdown
### Matrix 8: [Your Institution] Specific Skills

| Skill | L1 | L2 | L3 | L4 |
|-------|----|----|----|----|
| Domain-specific tool | | | | |
| Required platform | | | | |
```

**Adjust proficiency levels:**
- More rigorous: Require L3 for more skills by M4
- More accessible: Accept L2 in advanced skills

**Domain-specific versions:**
- Healthcare track: Add HIPAA, clinical data skills
- Finance track: Add risk modeling, regulatory compliance
- Social impact: Add ethics, policy analysis

### Student Resources Section

The document includes:
- Recommended learning paths for each competency
- Books, courses, tutorials by skill and level
- How to demonstrate each competency
- Portfolio development guidance

**Encourage students to:**
- Use resources proactively
- Share additional resources they find
- Contribute to a class resource list

---

## Complete Integration Example

Here's how to use all materials together for a comprehensive capstone program:

### Pre-Semester (Weeks -8 to 0)

**Week -8:**
- Announce capstone to registered students
- Share `capstone_prerequisites_appendix.tex` slides as PDF
- Share `COMPETENCY_MATRICES.md` for self-assessment
- Students complete initial competency assessment

**Week -6:**
- Students with gaps begin 8-week prep plan
- Weekly check-ins via course forum
- Share relevant learning resources

**Week -2:**
- Students complete final prep project
- Re-assess competencies
- Instructor reviews readiness

**Week 0:**
- First class: Present prerequisites slides (live)
- Discuss competency expectations
- Students set initial learning goals

### During Semester (Weeks 1-14)

**Weekly:**
- Students work on capstone (13-20 hrs/week)
- Track competencies in weekly logs
- Office hours for help

**Milestone Reviews:**
- Week 3 (M1): Assess foundational competencies
- Week 6 (M2): Assess modeling competencies
- Week 10 (M3): Assess advanced competencies
- Week 13 (M4): Assess production competencies

**Mid-Semester (Week 7):**
- Formal competency reassessment
- Individual meetings to discuss progress
- Adjust goals if needed

**Final Week (Week 14):**
- Final presentations with industry mentors
- Complete final competency assessment
- Portfolio planning session

### Post-Semester

**Week 15:**
- Students create portfolio showcasing competencies
- Update resumes with competency-based bullets
- Request recommendation letters (instructor references specific competencies)

**Ongoing:**
- Students use competency framework for job search
- Share capstone project in interviews
- Continue skill development

---

## Troubleshooting Common Issues

### Prerequisites Issues

**Issue:** Students feel overwhelmed by prerequisites
**Solution:** Emphasize "just-in-time learning" slides; not everything needed upfront

**Issue:** Wide variation in student background
**Solution:** Use learning paths to personalize preparation; consider tiered projects

**Issue:** Students don't take self-assessment seriously
**Solution:** Make it required; use results in first assignment (reflection essay)

### Competency Matrices Issues

**Issue:** Students don't update matrices regularly
**Solution:** Build into weekly submissions; requires weekly competency log (1 paragraph)

**Issue:** Students over/underestimate their level
**Solution:** Provide concrete examples; calibrate with peer discussion; instructor feedback

**Issue:** Too time-consuming to track all competencies
**Solution:** Focus on 10-15 core competencies; full assessment only at weeks 0, 7, 14

**Issue:** Hard to demonstrate competency growth
**Solution:** Use portfolio artifacts; code comparisons (M1 vs M4); presentation recordings

---

## Contact and Support

For questions about this enhancement module:
- **GitHub Issues:** [Your repo URL]
- **Course Slack:** #capstone-projects
- **Instructor:** [Your email]

---

## Version History

**v1.1** (January 2025)
- Added prerequisites appendix (8 slides)
- Added comprehensive competency matrices (7 matrices, 50+ skills)
- Added complete integration guide for all materials
- Added troubleshooting section

**v1.0** (January 2025)
- Initial release
- 30 slides covering 6 major sections
- 12 knowledge check frames with MCQs, conceptual problems, and coding challenges
- Integration guide for multiple course types
- 50+ bibliography references

---

## License

This enhancement module is released under [Your License]. Free to use and adapt for educational purposes with attribution.

---

**Happy teaching! Your students will build amazing capstone projects.**
