# Quiz Materials

**Topic-specific quizzes for knowledge assessment**

## 📚 Overview

This directory contains quizzes designed to assess student understanding of core concepts covered in each presentation topic. Quizzes are formative assessments that provide regular feedback to both students and instructors.

## 🎯 Quiz Design Principles

1. **Aligned with Learning Objectives**
   - Each question maps to specific learning objectives
   - Coverage across Bloom's taxonomy levels
   - Focus on understanding, not memorization

2. **Balanced Difficulty**
   - Mix of easy, medium, and hard questions
   - Progressive difficulty within quiz
   - Challenge without overwhelming

3. **Multiple Question Types**
   - Multiple choice (conceptual understanding)
   - Short answer (definitions, explanations)
   - Problem-solving (calculations, derivations)
   - True/False with justification

4. **Actionable Feedback**
   - Detailed answer explanations
   - Common misconceptions addressed
   - References to relevant materials

## 📋 Available Quizzes

### Deep Learning Quiz
- **File:** `deep_learning_quiz.tex` / `.pdf`
- **Topics:** Neural networks, backpropagation, CNN, RNN, Transformers
- **Questions:** 20 (15 MC, 5 short answer)
- **Duration:** 45 minutes
- **Difficulty:** Intermediate to Advanced

### Reinforcement Learning Quiz
- **File:** `reinforcement_learning_quiz.tex` / `.pdf`
- **Topics:** MDPs, Bellman equations, Q-learning, policy gradients
- **Questions:** 18 (12 MC, 6 short answer)
- **Duration:** 40 minutes
- **Difficulty:** Advanced

### Explainable AI Quiz
- **File:** `explainable_ai_quiz.tex` / `.pdf`
- **Topics:** SHAP, LIME, fairness, interpretability methods
- **Questions:** 15 (10 MC, 5 short answer)
- **Duration:** 35 minutes
- **Difficulty:** Intermediate

### Time Series Quiz
- **File:** `time_series_quiz.tex` / `.pdf`
- **Topics:** Stationarity, ARIMA, VAR, forecasting
- **Questions:** 18 (12 MC, 6 short answer)
- **Duration:** 40 minutes
- **Difficulty:** Intermediate

### Optimization Quiz
- **File:** `optimization_quiz.tex` / `.pdf`
- **Topics:** Convexity, gradient descent, KKT conditions
- **Questions:** 16 (10 MC, 6 short answer)
- **Duration:** 40 minutes
- **Difficulty:** Advanced

### MCMC Methods Quiz
- **File:** `mcmc_quiz.tex` / `.pdf`
- **Topics:** Bayesian inference, M-H, HMC, diagnostics
- **Questions:** 15 (10 MC, 5 short answer)
- **Duration:** 35 minutes
- **Difficulty:** Advanced

### Bayesian ML Quiz
- **File:** `bayesian_ml_quiz.tex` / `.pdf`
- **Topics:** Priors, posteriors, Gaussian processes, VI
- **Questions:** 16 (11 MC, 5 short answer)
- **Duration:** 35 minutes
- **Difficulty:** Advanced

### Causal Inference Quiz
- **File:** `causal_inference_quiz.tex` / `.pdf`
- **Topics:** DAGs, IV, RDD, DiD, propensity scores
- **Questions:** 18 (12 MC, 6 short answer)
- **Duration:** 40 minutes
- **Difficulty:** Advanced

## 📝 Quiz Format

### Question Types

**1. Multiple Choice**
```
Which of the following is TRUE about gradient descent?

A) It always finds the global minimum
B) It requires convexity to converge
C) Learning rate affects convergence speed
D) It cannot be used for neural networks

Answer: C
Explanation: Learning rate is crucial for convergence speed...
```

**2. Short Answer**
```
Explain the vanishing gradient problem in deep neural networks.
(3-4 sentences)

Sample Answer: The vanishing gradient problem occurs when...
```

**3. True/False with Justification**
```
True or False: SHAP values always sum to the model prediction.
Justify your answer.

Answer: True
Justification: By the additivity property of Shapley values...
```

**4. Problem-Solving**
```
Given the following MDP, compute the optimal value function...

Solution: Using value iteration...
```

## 🎓 Using Quizzes

### For Educators

**Before Quiz:**
1. Review quiz to ensure alignment with lectures
2. Adjust time limits based on class level
3. Decide on open book vs closed book
4. Share learning objectives with students

**During Quiz:**
1. Provide quiet environment
2. Clarify questions if needed
3. Monitor time
4. Ensure academic integrity

**After Quiz:**
1. Grade promptly (within 1 week)
2. Provide answer key
3. Discuss common mistakes
4. Identify topics needing review

**Customization:**
- Modify questions to match emphasis
- Add/remove questions
- Adjust difficulty level
- Include course-specific examples

### For Students

**Preparation:**
1. Review learning objectives
2. Study presentation slides
3. Complete self-assessment checklist
4. Practice similar problems
5. Form study groups

**During Quiz:**
1. Read questions carefully
2. Start with easier questions
3. Show your work
4. Check answers if time permits
5. Don't panic if stuck

**After Quiz:**
1. Review feedback thoroughly
2. Understand mistakes
3. Ask questions in office hours
4. Note patterns for future study

## 📊 Grading Guidelines

### Point Allocation

**Multiple Choice (5 points each):**
- Correct: 5 points
- Incorrect: 0 points
- No partial credit

**Short Answer (10 points each):**
- Excellent (9-10): Complete, accurate, well-explained
- Good (7-8): Mostly correct, minor gaps
- Satisfactory (5-6): Partially correct, significant gaps
- Poor (0-4): Incorrect or incomplete

**Problem-Solving (15-20 points each):**
- Correct answer + work (100%)
- Correct approach, minor error (70-90%)
- Partially correct approach (40-60%)
- Minimal understanding (10-30%)
- No attempt or completely wrong (0%)

### Grading Rubric

| Score | Grade | Criteria |
|-------|-------|----------|
| 90-100 | A | Excellent understanding |
| 80-89 | B | Good understanding, minor gaps |
| 70-79 | C | Satisfactory, some gaps |
| 60-69 | D | Limited understanding |
| 0-59 | F | Insufficient understanding |

## 📈 Performance Analysis

### For Instructors

Track quiz performance to:
- Identify difficult concepts
- Adjust teaching emphasis
- Compare across topics
- Predict exam performance

**Useful Metrics:**
- Average score per quiz
- Question difficulty (% correct)
- Time to completion
- Performance by question type

### For Students

Use quiz results to:
- Identify weak areas
- Guide study focus
- Track improvement
- Prepare for exams

## 🔧 Creating New Quizzes

### Quiz Template Structure

```latex
\documentclass{exam}
\usepackage{../theme/esmad_exam_template}

\title{Topic Name Quiz}
\date{\today}

\begin{document}

\maketitle

\begin{questions}

\question[5] Multiple choice question...
\begin{choices}
\choice Option A
\choice Option B
\correctchoice Option C
\choice Option D
\end{choices}

\question[10] Short answer question...
\vspace{3cm}

\end{questions}

\end{document}
```

### Best Practices

1. **Clear Questions**
   - Unambiguous wording
   - Specific, focused questions
   - Avoid trick questions

2. **Balanced Difficulty**
   - 30% easy (recall, recognition)
   - 50% medium (application, analysis)
   - 20% hard (synthesis, evaluation)

3. **Fair Assessment**
   - Test concepts covered in class
   - Reasonable time limits
   - Clear instructions

4. **Good Distractors** (for MC)
   - Plausible incorrect options
   - Address common misconceptions
   - Not obviously wrong

## 📚 Study Resources

Point students to:
- Presentation slides
- Code examples in `../../code/`
- Exercises in `../../exercises/`
- Self-assessment checklists
- Office hours

## 📧 Contact

For questions about quizzes:
- **Instructor:** Diogo Ribeiro
- **Email:** dfr@esmad.ipp.pt
- **Issues:** [GitHub Issues](https://github.com/diogoribeiro7/academic-presentations/issues)

## 📄 License

**Quizzes:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

---

*Last Updated: January 2025*
*Part of the Academic Presentations series*
