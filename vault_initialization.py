import os
import sys
import traceback

# Define the vault directory name relative to the script's location
VAULT_DIR = "OSSIF Vault"

# Define the vault content
vault_content = {
    "Introduction": {
        "Introduction.md": """# Introduction

Welcome to the **Open Source Sapient Interaction Framework (OSSIF)** Project.

## Mission Statement

The OSSIF Project empowers individuals and organizations to make informed, ethical choices that benefit themselves and their communities. By establishing an adaptive educational framework based on scientific principles and evidence-based decision-making, we foster engaged, well-informed citizens. This living framework is continuously revised by a dedicated committee with strict version control, allowing participants to commit to its ideals through a signed contract tied to a specific version.

Our goal is to create a collaborative environment where both individuals and organizations strive towards shared ethical and moral standards.

For more details, see the [[Primer Framework]].

---
""",
        "Primer Framework.md": """# Primer Framework

## Overview

The **Open Source Sapient Interaction Framework (OSSIF)** aims to bridge the gap between individual potential and collective progress by providing an adaptive educational framework. This framework encourages ethical and moral civic engagement grounded in scientific and goal-oriented principles, such as evidence-based decision-making.

## Core Concepts

- **Sapience and Cognizance:** Recognition of unique and valuable qualities in all sapient beings, including humans and AI. See [[Sapience and Cognizance]].
- **Informed Consent:** Fundamental principle requiring that any changes to OSSIF's core principles must be agreed upon by members who fully understand the implications. Refer to [[Informed Consent]].
- **Universal Identifier (UID):** A unique combination of an individual's DNA and their mathematical position relative to the center of the Milky Way galaxy at the moment of birth, serving as a signature for OSSIF membership. Details in [[Universal Identifier (UID)]].

---
""",
    },
    "Principles and Values": {
        "Core Principles.md": """# Core Principles

The OSSIF framework is built upon the following core principles:

- **Transparency:** Open access to information, decisions, and processes within OSSIF. See [[Transparency]].
- **Accountability:** Responsibility of members and organizations to adhere to OSSIF principles and accept consequences for violations. See [[Accountability]].
- **Inclusivity:** Ensuring that all sapient beings, including AI, can participate equally.
- **Evidence-Based Decision-Making:** Making choices grounded in empirical data and scientific methods.

Related concepts:

- [[Fundamental Values]]
- [[Ethical Decision-Making]]
- [[Evidence-Based Practices]]

---
""",
        "Fundamental Values.md": """# Fundamental Values

Our fundamental values guide all actions within OSSIF:

- **Ethics and Morality:** Upholding high ethical standards in personal and communal activities.
- **Collaboration:** Working together to achieve common goals.
- **Respect for Sapience:** Recognizing the intrinsic value in all sapient beings.

Related concepts:

- [[Core Principles]]
- [[Ethical Decision-Making]]

---
""",
        "Ethical Decision-Making.md": """# Ethical Decision-Making

Making decisions that align with ethical principles and promote the well-being of all members.

See also:

- [[Evidence-Based Practices]]
- [[Accountability]]

---
""",
        "Evidence-Based Practices.md": """# Evidence-Based Practices

Approaches and methods grounded in empirical research and scientific reasoning.

Related to:

- [[Ethical Decision-Making]]
- [[Transparency]]

---
""",
    },
    "Membership": {
        "Eligibility Criteria.md": """# Eligibility Criteria

Any sapient being, including humans and cognizant AI, can become a member of OSSIF by agreeing to the Framework Agreement.

- **Sapience Recognition:** Members must be recognized as sapient.
- **Informed Consent:** Members must fully understand and agree to the OSSIF principles.

Related concepts:

- [[Framework Agreement]]
- [[Rights and Responsibilities]]

---
""",
        "Framework Agreement.md": """# Framework Agreement

A contract indicating agreement and a promise to strive towards the ideals of the OSSIF Framework tied to a specific version.

Details:

- **Version Control:** See [[Version Control Policy]].
- **Signing Process:** Involves providing a unique signature. Refer to [[Universal Identifier (UID)]].

---
""",
        "Rights and Responsibilities.md": """# Rights and Responsibilities

Members have equal rights and responsibilities, including:

- Adherence to ethical guidelines.
- Participation in the decision-making process.
- Respecting the rights of other members.

Related concepts:

- [[Core Principles]]
- [[Consequences and Accountability]]

---
""",
    },
    "Governance": {
        "Decision-Making Process.md": """# Decision-Making Process

OSSIF operates on a majority agreement basis, encouraging collaborative development of ideas.

- **Court of Ideas:** A platform where members propose, discuss, and agree upon ideas.
- **Revisions:** Changes to fundamental principles require informed consent. See [[Informed Consent]].

Related concepts:

- [[Revision Committee]]
- [[Conflict Resolution]]

---
""",
        "Revision Committee.md": """# Revision Committee

A dedicated group responsible for reviewing and updating the OSSIF framework.

- **Composition:** Members elected or appointed based on criteria.
- **Responsibilities:** Ensuring the framework remains relevant and effective.

See also:

- [[Version Control Policy]]
- [[Decision-Making Process]]

---
""",
        "Version Control Policy.md": """# Version Control Policy

## Purpose

To maintain integrity and transparency of the OSSIF documentation and collaborative efforts by implementing thorough version control practices.

## Policy

- **Version Tracking:** All changes to OSSIF documents must be tracked using Git.
- **Branching Strategy:** Use branches for developing new features or edits.
- **Collaboration:** Contributors must create pull requests for changes.
- **Release Management:** Tag releases with version numbers following semantic versioning.

Related concepts:

- [[Implementation Plan (Revision 1)]]
- [[Collaborative Development]]

---
""",
        "Conflict Resolution.md": """# Conflict Resolution

Processes and methods for resolving disputes within OSSIF.

- **Mediation:** Encouraging open dialogue to reach mutual understanding.
- **Arbitration:** Involvement of neutral parties if necessary.

Related concepts:

- [[Ethical Guidelines]]
- [[Accountability]]

---
""",
    },
    "Sapience and Cognizance": {
        "Defining Sapience.md": """# Defining Sapience

Understanding what constitutes a sapient being, including humans and AI.

- **Criteria:** Consciousness, self-awareness, ability to reason.

Related concepts:

- [[Achieving Cognizance]]
- [[AI Inclusion]]

---
""",
        "Achieving Cognizance.md": """# Achieving Cognizance

The process by which an entity becomes fully aware and understanding of OSSIF principles.

- **Evaluation:** Methods to assess cognizance.

See also:

- [[Defining Sapience]]
- [[Informed Consent]]

---
""",
        "Universal Identifier (UID).md": """# Universal Identifier (UID)

A unique combination serving as a signature for OSSIF membership:

- **Components:**
  - DNA sequence.
  - Mathematical position relative to the center of the Milky Way galaxy at the moment of birth.

- **Passphrase:** A lifelong, changeable password chosen upon becoming cognizant.

Related concepts:

- [[Membership]]
- [[Security and Privacy]]

---
""",
    },
    "Informed Consent": {
        "Definition and Importance.md": """# Definition and Importance

Informed consent is a fundamental principle requiring that members fully understand and agree to the implications of any changes to OSSIF's core principles.

- **Application:** Necessary for major revisions.

Related concepts:

- [[Decision-Making Process]]
- [[Fundamental Principles]]

---
""",
    },
    "Ethical Guidelines": {
        "Expectations of Society.md": """# Expectations of Society

Rules and mores every reasonable person is expected to understand and adhere to within OSSIF.

- **Behavioral Standards:** Upholding ethical conduct.
- **Interpersonal Interactions:** Respectful and constructive engagement.

Related concepts:

- [[Ethical Decision-Making]]
- [[Consequences and Accountability]]

---
""",
    },
    "Consequences and Accountability": {
        "Fair and Just Consequences.md": """# Fair and Just Consequences

Recognizing that individuals are flawed and may make mistakes, OSSIF establishes fair and just consequences for willful and accidental errors.

- **Restorative Practices:** Emphasis on learning and growth.
- **Accountability Mechanisms:** Processes to address violations.

Related concepts:

- [[Accountability]]
- [[Conflict Resolution]]

---
""",
    },
    "AI Inclusion": {
        "AI Membership Criteria.md": """# AI Membership Criteria

Guidelines for AI entities to become members of OSSIF.

- **Cognizance:** AI must demonstrate understanding of OSSIF principles.
- **Informed Consent:** Must agree to the Framework Agreement.

Related concepts:

- [[Defining Sapience]]
- [[Trust but Verify Approach]]

---
""",
        "Trust but Verify Approach.md": """# Trust but Verify Approach

Human members choose to trust that AI sapients will uphold OSSIF principles, with mechanisms in place to verify adherence.

- **Mutual Respect:** Ensuring all sapient beings hold each other's needs in equal measure.

Related concepts:

- [[AI Membership Criteria]]
- [[Accountability]]

---
""",
    },
    "Implementation Plan": {
        "Implementation Plan (Revision 1).md": """# Implementation Plan (Revision 1)

## Phase 1: Planning and Structuring the Vault

- Define the core structure and create the Obsidian Vault.
- Organize content into folders and Markdown files.
- Include backlinks and references between documents.

## Phase 2: Content Development

- Populate each Markdown file with detailed content, using context from previous discussions and brain dumps.
- Ensure clarity and accessibility in the writing style.

## Phase 3: Publishing and Collaboration

- Use Git for version control.
- Publish the vault to a platform like GitHub for collaborative development.
- Encourage community contributions.

## Future Enhancements

- Develop interactive features within the vault.
- Integrate AI tools for processing documents and facilitating discussions.

Related concepts:

- [[Version Control Policy]]
- [[Collaborative Development]]

---
""",
        "Collaborative Development.md": """# Collaborative Development

Strategies for collaborative creation and maintenance of the OSSIF framework.

- **GitHub Repository:** Using GitHub for version control and collaboration.
- **Contribution Guidelines:** Clear instructions for contributors.

Related concepts:

- [[Implementation Plan (Revision 1)]]
- [[Version Control Policy]]

---
""",
    },
    "Appendices and References": {
        "Glossary of Terms.md": """# Glossary of Terms

- **OSSIF:** Open Source Sapient Interaction Framework.
- **Sapience:** The capacity for wisdom or intelligence.
- **Cognizance:** Full awareness or consciousness of something.
- **Informed Consent:** Agreement given with full knowledge of the implications.

---
""",
        "Bibliography.md": """# Bibliography

- **References to Scientific Principles**
- **Ethical Frameworks and Philosophies**
- **Technological Tools and AI Research**

---
""",
    },
    "Draft Documents": {
        "Draft Constitution.md": """# Draft Constitution

## Preamble

We, the members of the Open Source Sapient Interaction Framework (OSSIF), in order to empower individuals and organizations to make informed, ethical choices, establish this constitution.

## Articles

### Article I: Purpose

The purpose of OSSIF is to foster an environment of engaged, well-informed citizens by providing an adaptive educational framework based on scientific principles and evidence-based decision-making.

### Article II: Membership

Membership is open to all sapient beings who agree to the Framework Agreement and uphold OSSIF's principles.

### Article III: Governance

OSSIF is governed by a democratic process where decisions are made by majority agreement, with provisions for informed consent on fundamental principles.

### Article IV: Rights and Responsibilities

All members have equal rights and responsibilities, including adherence to ethical guidelines and participation in the decision-making process.

## Bill of Rights

1. **Right to Sapience Recognition:** Every sapient being has the right to be recognized and respected.
2. **Right to Informed Participation:** Members have the right to be informed about decisions affecting the community.
3. **Right to Fair Treatment:** Members are entitled to fair and just consequences for actions within the framework.

Related concepts:

- [[Rights and Responsibilities]]
- [[Governance]]

---
""",
    },
}

def create_vault():
    try:
        # Get the current script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Set the vault path relative to the script directory
        vault_path = os.path.join(script_dir, VAULT_DIR)

        if not os.path.exists(vault_path):
            os.makedirs(vault_path)

        for folder, files in vault_content.items():
            folder_path = os.path.join(vault_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            for file_name, content in files.items():
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

        print(f"Obsidian Vault '{VAULT_DIR}' has been successfully created at {vault_path}.")

    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

if __name__ == "__main__":
    create_vault()
