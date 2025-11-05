# Exam Materials

**Midterm and final exam templates and resources**

## 📚 Overview

This directory contains exam templates, sample exams, and resources for conducting midterm and final assessments. Exams are designed to comprehensively evaluate student understanding across multiple topics.

## 🎯 Exam Philosophy

Our exams are designed to:

1. **Assess Comprehensive Understanding**
   - Integration across topics
   - Application to new scenarios
   - Critical thinking and analysis

2. **Balance Multiple Skill Levels**
   - Recall and recognition (20%)
   - Application and analysis (50%)
   - Synthesis and evaluation (30%)

3. **Provide Fair Assessment**
   - Align with learning objectives
   - Reasonable time limits
   - Clear instructions and expectations

4. **Promote Deep Learning**
   - Discourage memorization
   - Reward understanding and reasoning
   - Allow demonstration of mastery

## 📋 Exam Structure

### Midterm Exam

**Coverage:** First half of course
- Deep Learning
- Optimization
- Statistical Learning
- Feature Engineering

**Format:**
- **Duration:** 2-3 hours
- **Points:** 100 total
- **Format:** Open book, closed internet
- **Sections:**
  1. Multiple Choice (20 points)
  2. Short Answer (30 points)
  3. Problem Solving (30 points)
  4. Essay/Analysis (20 points)

**Files:**
- `midterm_exam_template.tex` - LaTeX template
- `sample_exams/midterm_sample_1.pdf` - Example exam
- `sample_exams/midterm_solution_1.pdf` - Solutions

### Final Exam

**Coverage:** Entire course (emphasis on second half)
- Reinforcement Learning
- Time Series Analysis
- Explainable AI
- Causal Inference
- MCMC and Bayesian ML

**Format:**
- **Duration:** 3 hours
- **Points:** 100 total
- **Format:** Open book, closed internet
- **Sections:**
  1. Multiple Choice (15 points)
  2. Short Answer (25 points)
  3. Problem Solving (40 points)
  4. Integration Question (20 points)

**Files:**
- `final_exam_template.tex` - LaTeX template
- `sample_exams/final_sample_1.pdf` - Example exam
- `sample_exams/final_solution_1.pdf` - Solutions

## 📝 Question Types

### 1. Multiple Choice (20%)

**Purpose:** Test breadth of knowledge

**Example:**
```
Which statement about Q-learning is TRUE?

A) It is an on-policy algorithm
B) It requires a model of the environment
C) It learns the optimal Q-function directly
D) It cannot handle continuous state spaces

Answer: C
```

**Grading:**
- No partial credit
- Typically 3-5 points per question

### 2. Short Answer (25-30%)

**Purpose:** Test conceptual understanding

**Example:**
```
Q: Explain why batch normalization helps deep neural
   networks train faster. (5 points)

A: Batch normalization reduces internal covariate shift by
   normalizing layer inputs. This stabilizes the distribution
   of activations, allowing higher learning rates and faster
   convergence...
```

**Grading:**
- Partial credit based on completeness and accuracy
- Typically 5-10 points per question

### 3. Problem Solving (30-40%)

**Purpose:** Test application and analytical skills

**Example:**
```
Q: Given the following time series data, fit an ARIMA(1,1,1)
   model and forecast the next 3 time steps. Show your work.

Data: [12, 14, 13, 16, 18, 17, 19, ...]

A: [Step-by-step solution with calculations]
```

**Grading:**
- Partial credit for correct approach
- Full credit requires correct answer + work
- Typically 10-20 points per question

### 4. Essay/Integration Questions (20%)

**Purpose:** Test synthesis and critical thinking

**Example:**
```
Q: Compare and contrast SHAP and LIME for explaining ML
   models. Discuss when you would use each method and
   their respective advantages and limitations. (20 points)

A: [Detailed comparative analysis]
```

**Grading:**
- Rubric-based assessment
- Evaluates depth, accuracy, organization, clarity

## 🎓 Exam Administration

### Before the Exam

**For Instructors:**
1. Review and customize exam template
2. Prepare answer key
3. Set up exam environment
4. Communicate expectations clearly
5. Provide practice problems

**For Students:**
1. Review all learning objectives
2. Complete self-assessment checklists
3. Practice past exams
4. Attend review sessions
5. Prepare allowed materials

### During the Exam

**Allowed Materials:**
- Course notes and slides
- Textbooks and references
- Calculator
- Formula sheets (if provided)

**NOT Allowed:**
- Internet access
- Communication with others
- AI tools (ChatGPT, etc.)
- Previous exams (unless provided)

**Exam Conduct:**
- Arrive early
- Bring ID
- Follow honor code
- Ask clarifying questions
- Manage time wisely

### After the Exam

**Grading Timeline:**
- Return within 2 weeks
- Provide detailed feedback
- Share grade distribution

**Review Process:**
- Review session to discuss answers
- Office hours for individual questions
- Regrade requests (if applicable)

## 📊 Grading Rubric

### Overall Grading Scale

| Score | Grade | Performance Level |
|-------|-------|------------------|
| 93-100 | A | Outstanding mastery |
| 90-92 | A- | Excellent understanding |
| 87-89 | B+ | Very good understanding |
| 83-86 | B | Good understanding |
| 80-82 | B- | Satisfactory understanding |
| 77-79 | C+ | Adequate understanding |
| 73-76 | C | Acceptable understanding |
| 70-72 | C- | Minimal understanding |
| 60-69 | D | Limited understanding |
| 0-59 | F | Insufficient understanding |

### Problem-Solving Rubric

**Full Credit (100%):**
- Correct approach
- Accurate calculations
- Correct final answer
- Work clearly shown

**Substantial Credit (70-90%):**
- Correct approach
- Minor calculation errors
- Work clearly shown

**Partial Credit (40-60%):**
- Partially correct approach
- Significant errors
- Some understanding demonstrated

**Minimal Credit (10-30%):**
- Incorrect approach
- Minimal understanding
- Some relevant attempt

**No Credit (0%):**
- No attempt
- Completely incorrect
- Plagiarism

## 🔧 Creating Custom Exams

### Using the Templates

**Midterm Template:**
```latex
\documentclass[12pt]{exam}
\usepackage{../theme/esmad_exam_template}

\title{Midterm Exam - Course Name}
\date{Semester Year}

\begin{document}
\maketitle

\begin{center}
\fbox{\fbox{\parbox{5.5in}{\centering
Instructions and policies}}}
\end{center}

\begin{questions}
% Your questions here
\end{questions}

\end{document}
```

**Customization Guidelines:**

1. **Adjust Difficulty**
   - Consider class performance on quizzes
   - Balance easy/medium/hard questions
   - Ensure adequate time

2. **Select Topics**
   - Cover material emphasized in lectures
   - Include recent and foundational topics
   - Balance breadth and depth

3. **Point Allocation**
   - Weight by topic importance
   - Consider time per question
   - Ensure fair distribution

4. **Provide Context**
   - Clear problem statements
   - Necessary formulas/data
   - Appropriate level of scaffolding

### Quality Checklist

Before finalizing exam:
- [ ] All questions aligned with learning objectives
- [ ] Difficulty appropriate for time limit
- [ ] Instructions clear and unambiguous
- [ ] Answer key complete
- [ ] No errors in questions or data
- [ ] Fair assessment of course content
- [ ] Balanced coverage of topics
- [ ] Reasonable point distribution

## 📚 Study Resources

### Preparation Materials

**Provided to Students:**
- Practice exams
- Review sessions
- Study guides
- Formula sheets
- Past quiz solutions

**Self-Study:**
- Presentation slides
- Code examples
- Problem sets
- Self-assessment checklists
- Textbook chapters

### Study Tips

**Effective Preparation:**
1. Start early (2-3 weeks before)
2. Review all topics systematically
3. Practice problem-solving
4. Form study groups
5. Attend review sessions
6. Get adequate sleep

**During Exam:**
1. Read all instructions carefully
2. Budget time wisely
3. Start with easier questions
4. Show all work
5. Review answers if time permits

## 📈 Performance Analysis

### For Instructors

**Post-Exam Analysis:**
- Calculate grade distribution
- Identify difficult questions
- Assess topic mastery
- Compare to previous years
- Adjust future teaching

**Useful Metrics:**
- Mean, median, standard deviation
- Question difficulty (% correct)
- Score distribution by topic
- Time to completion

### For Students

**Using Exam Results:**
- Identify weak areas
- Understand mistakes
- Apply to future study
- Seek help as needed

## 📧 Contact

For questions about exams:
- **Instructor:** Diogo Ribeiro
- **Email:** dfr@esmad.ipp.pt
- **Office Hours:** By appointment
- **Issues:** [GitHub Issues](https://github.com/diogoribeiro7/academic-presentations/issues)

## 📄 License

**Exam Materials:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

**Academic Integrity:**
- Do not share exams publicly
- Use only for authorized educational purposes
- Follow institutional policies

---

*Last Updated: January 2025*
*Part of the Academic Presentations series*
