# Spec-Driven Development (SDD) with Spec-Kit

This document outlines the principles of Spec-Driven Development (SDD) and how to use the GitHub Spec-Kit toolkit to implement it effectively.

## 1. The Problem with Unstructured Development ("Vibe Coding")

Traditionally, software development, especially with LLMs, can be an unstructured process. It often looks like this:

1.  A vague prompt is given: e.g., *"Build a podcast website."*
2.  The LLM generates code based on its interpretation.
3.  The result is a mix of desired and undesired outcomes.
4.  This leads to a cycle of numerous change requests.
5.  The final output often suffers from messy code, logical drift, and a mismatch with the original expectations.

This common anti-pattern is a result of **imprecision** and leads developers down unproductive **rabbit holes**.

## 2. Introducing Spec-Driven Development (SDD)

The core philosophy of SDD is simple:

> **"Think First, Code Later."**

Instead of treating an LLM as a magic coder, SDD encourages treating it like a **junior engineer** who requires clear, well-defined instructions to be effective. The process involves a structured, top-down approach:

1.  **Define WHAT & WHY**: Start with a clear business or product vision.
2.  **Decide HOW**: Create a technical plan based on engineering best practices.
3.  **Create TASKS**: Break down the plan into small, executable steps.
4.  **Write Code**: Execute the tasks to build the software.

## 3. The Four Core Artifacts of SDD

SDD operates in four distinct layers, each producing a key artifact.

### I. The Constitution

The Constitution contains the **non-negotiable rules** of the project. These are high-level principles that govern all development work.

-   **Examples**:
    -   "The project must always be a static site."
    -   "Unit tests are mandatory for all new features."
    -   "The final product must meet WCAG 2.1 AA accessibility standards."
    -   "No backend server is to be used; rely on serverless functions."

> **Analogy**: Think of the Constitution as the fundamental laws of the project. Everyone, whether a human or an AI, must follow them without exception.

### II. The Specification (Spec)

The Spec is the **WHAT & WHY** document. It is typically authored from a Product Manager's perspective and focuses entirely on the user and business goals.

-   **It includes**:
    -   User goals and stories.
    -   Key features.
    -   Acceptance criteria for each feature.
    -   Potential edge cases.
-   **It excludes**:
    -   Implementation details like frameworks, languages, or libraries.

> **Analogy**: The Spec clarifies *what* needs to be built and *why*, but intentionally defers the question of *how* it will be built.

### III. The Plan

The Plan is the **HOW** document. This is where engineering decisions are made to translate the *what* from the Spec into a concrete technical strategy.

-   **It includes**:
    -   The chosen tech stack (e.g., React, Python, Node.js).
    -   High-level architecture diagrams.
    -   Data models and schemas.
    -   Hosting and deployment assumptions.
    -   Quality gates and testing strategies.

> **Analogy**: This is the engineer's blueprint. It provides a detailed technical guide for bringing the Specification to life.

### IV. The Tasks

Tasks are the final, **executable steps** derived from the Plan. They are granular, ordered, and designed to be followed by either a human developer or an LLM.

-   **Characteristics**:
    -   Follow a test-first (TDD) approach where applicable.
    -   Are ordered logically to ensure a smooth build process.
    -   Are clear and unambiguous.

> **Analogy**: Tasks break the work down into a manageable construction sequence: first the foundation, then the walls, and finally the paint.

## 4. What is GitHub Spec-Kit?

**Spec-Kit** is a toolkit developed and open-sourced by GitHub. It is designed to make the Spec-Driven Development process **practical, repeatable, and scalable.**

It brings structure to the potential chaos of LLM-driven development by providing a concrete implementation of the SDD workflow.

> **Important**: Spec-Kit is not a rigid framework. It is a flexible combination of **processes, prompts, and scripts** that you can adapt to your project's needs.

## 5. Key Components of Spec-Kit

### 📂 `.github/prompts/`

This directory contains the prompt definitions for slash commands (e.g., `/specify`, `/plan`). These prompts are crucial for guiding the LLM. They tell the model exactly:

-   What context files to read.
-   Which templates to use for its response.
-   Which scripts to execute to perform actions.

### 📂 `specify/`

This directory is the heart of the Spec-Kit configuration and contains:

-   `memory/constitution.md`: The stored project Constitution.
-   `templates/`: A collection of reusable markdown templates for generating Specs, Plans, etc.
-   `scripts/` (PowerShell/bash): A set of scripts to automate deterministic actions like creating files, running builds, or managing git branches.

> **Why Scripts are Important**: Scripts are deterministic. They ensure that key actions are performed predictably and reliably, removing the need for the LLM to guess and reducing the chance of errors.

## 6. Core Spec-Kit Commands

These are the essential commands used in the SDD workflow with Spec-Kit.

| Command                 | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| `/speckit.constitution` | Create or update the project's governing principles.                     |
| `/speckit.specify`      | Define what you want to build (requirements and user stories).           |
| `/speckit.plan`         | Create a technical implementation plan with your chosen tech stack.      |
| `/speckit.tasks`        | Generate an actionable, step-by-step task list for implementation.       |
| `/speckit.implement`    | Execute all tasks to build the feature according to the plan.            |

## 7. Note on `/speckit.implement` Command

`Spec-Kit formalizes the first four phases and intentionally leaves the fifth phase — implementation — under human control, as it is a critical practice.`

### Why Spec-Kit Does Not Fully Automate Implementation

1.  **Implementation Is Iterative, Not Atomic**
    Implementation is not a single, atomic action. It is inherently:
    *   Incremental
    *   Reversible
    *   Test-driven
    *   Often interrupted by review and correction

    A single `/implement` command would encourage large, uncontrolled changes, which goes against these principles.

2.  **Safety and Blast-Radius Control**
    A global "implement everything" command would:
    *   Modify too many files at once, making review difficult.
    *   Make debugging challenging due to the scope of changes.
    *   Increase the risk of violating the project's Constitution or Specification.

    Spec-Kit is designed to limit the "blast radius" of changes, ensuring more controlled development.

3.  **Human-in-the-Loop Is Mandatory**
    During the implementation phase, human developers must be able to:
    *   Switch between different models or tools.
    *   Pause or stop execution at any point.
    *   Modify tasks or specifications as new insights emerge.
    *   Review changes incrementally before committing.

    Full automation at this stage would significantly reduce essential human control and oversight.

4.  **Code Is Disposable; Specs Are Not**
    A core philosophy of Spec-Kit is that while **specifications and plans are durable artifacts, implementations are disposable.**
    By keeping implementation outside a formal command, Spec-Kit allows you to:
    *   Easily delete generated code.
    *   Switch LLMs or development approaches.
    *   Re-implement features from the same validated Spec and Plan.

    This flexibility is a critical capability for agile and resilient development.

### How Implementation Actually Works in Spec-Kit

Implementation is performed by executing tasks one at a time, often in a conversational, iterative manner with an AI agent.

A typical interaction might look like this:

-   "Implement Task 1 only. Update the task status. Do not proceed to the next task."
-   "Implement Task 2. Fix any failing tests. Update `tasks.md`."

In this model:
*   **Tasks** act as executable contracts.
*   **Implementation** is the controlled and incremental execution of those contracts, with continuous human supervision.

## 8. Integrating Google ADK using Spec-Kit

Spec-Kit's structured process is ideal for developing on complex platforms like the **Google Assistant Development Kit (ADK)**.

### Constitution

Your Constitution can include rules specific to Google ADK development to ensure consistency.

-   **Example Rules**:
    -   "All conversational actions must follow official Google ADK design patterns."
    -   "Fulfillment logic must be deployed as a serverless Cloud Function."

### Specification

The Spec remains focused on the user's conversational goals, defining user journeys and dialogues without mentioning the ADK itself.

-   **Example**: "As a user, I want to be able to order a pizza by specifying the size and toppings, so that I can quickly place my order via voice."

### Plan

The Plan is where the Google ADK is explicitly chosen as the technology to implement the Spec.

-   **The Plan would detail**:
    -   The decision to use the Google ADK for building the conversational action.
    -   A mapping of features from the Spec to ADK components (e.g., Intents, Types, Scenes).
    -   The architecture for the fulfillment webhook (e.g., Node.js on Cloud Functions).

### Tasks

The Plan is then broken down into concrete, ADK-specific tasks that an engineer or LLM can execute.

-   **Example Task List**:
    1.  Initialize a new project using the `gactions` CLI.
    2.  Define the `OrderPizza` intent and its training phrases in `sdk/intents/OrderPizza.yaml`.
    3.  Define the `PizzaSize` and `Toppings` types in `sdk/types/`.
    4.  Implement the webhook handler for the `OrderPizza` scene in `webhooks/main.js` using the `@google/assistant-sdk` library.
    5.  Write unit tests for the fulfillment logic to validate order processing.
    6.  Deploy the webhook to Google Cloud Functions.
