# PatchUp — HCI Project Idea Prompt

## Project Overview

PatchUp is a digital product concept for a Human-Computer Interaction project focused on how artificial intelligence can support local communities through community-based repair networks.[cite:118][cite:147][cite:153]

The core idea is an AI-assisted platform where a user photographs a broken household item, briefly describes the problem, and receives a structured repair assessment: likely fault type, repair difficulty, estimated chance of successful repair, whether the item is worth repairing, and the most suitable next step.[cite:146][cite:149][cite:152]

Instead of functioning as a generic “find a repair shop” app, PatchUp is designed as a decision-and-community system that bridges three things: AI diagnosis, repair pathway recommendation, and connection to local repair communities such as Repair Cafés, hobbyists, and community repair events.[cite:118][cite:143][cite:150]

## Why This Topic Fits the Course

This concept fits the broader topic of AI-powered digital solutions for local communities because repair communities already exist as local, volunteer-driven ecosystems centered on sustainability, learning, and mutual support.[cite:118][cite:145][cite:153]

It is also a strong HCI topic because the design challenge is not only technical accuracy, but also trust, explanation, usability for non-experts, and the coordination between human expertise and AI recommendations.[cite:149][cite:152]

## Core Problem

Many people throw away devices or objects that could still be repaired because they do not know what is broken, whether the repair is realistic, or where to get help locally.[cite:139][cite:153]

At the same time, community repair initiatives already provide support, but the path from “I have a broken item” to “I know what to do next” is still fragmented and intimidating for beginners.[cite:145][cite:147][cite:153]

PatchUp addresses that gap.

## Main Value Proposition

PatchUp helps a person move from confusion to action.

A user should be able to:
- scan a broken item,
- understand what might be wrong,
- decide whether repair is worthwhile,
- and be guided to the best repair path: DIY, a local repair event, or a community expert.[cite:146][cite:149][cite:152]

## AI Role in the Product

The AI layer must be central and visible.

It should not behave like a simple search filter or a chatbot. Instead, the AI should perform tasks that require interpretation of unstructured input such as photos and short free-text descriptions.[cite:146][cite:152]

### AI capabilities

1. **Object recognition**  
Identify the category of the item, such as lamp, toaster, fan, headphones, chair, bicycle component, or small appliance.[cite:146][cite:149]

2. **Problem inference**  
Estimate the likely issue based on the image and user description, for example: broken switch, loose cable, damaged casing, worn battery, detached component, or possible motor issue.[cite:146][cite:152]

3. **Repairability score**  
Estimate how repairable the item is, how difficult the repair may be, and how likely a successful outcome is.[cite:149][cite:152]

4. **Repair pathway recommendation**  
Recommend whether the user should try a beginner-level repair, attend a repair event, ask a skilled volunteer, or stop and reuse the item for parts.[cite:147][cite:150][cite:153]

5. **Community matching**  
Connect the user to the most relevant local repair pathway based on item type, skill needed, distance, event availability, and community expertise.[cite:118][cite:143][cite:147]

## Product Vision

PatchUp is not just an app for fixing objects.

It is a platform that supports a local culture of repair by making repair more understandable, less intimidating, and more social.[cite:118][cite:145][cite:153]

The product should communicate the idea that repair is not only about saving money, but also about reducing waste, learning practical skills, and connecting with people in the local community.[cite:139][cite:145]

## Target Users

### 1. Everyday user

A person with a broken item who has little or no technical knowledge and wants quick, understandable guidance.

### 2. Community repair volunteer

A hobbyist or skilled helper who can repair certain categories of items and is willing to support others through events or direct assistance.[cite:145][cite:147]

### 3. Repair event organizer

A person or organization managing local repair sessions who wants better triage, clearer repair cases, and more efficient matching between users and volunteers.[cite:118][cite:147]

## Main User Scenario

A user has a broken small appliance at home.

They open PatchUp, take a photo, describe the issue in one sentence, and receive an AI-generated result page that explains what the likely problem is, how complex the repair might be, and what the recommended next step is.[cite:146][cite:149][cite:152]

If the issue appears simple, the app can direct the user toward a beginner-friendly repair path. If the issue is moderate or uncertain, the app can suggest a nearby repair event. If the issue requires more advanced knowledge, the app can route the case toward someone in the community with the right skills.[cite:143][cite:147][cite:150]

## Key Features

### 1. Broken item scan

- Photo upload or camera capture
- Short text input describing symptoms
- Optional category selection if the AI is uncertain

### 2. AI diagnosis card

- Item recognized
- Probable issue
- Difficulty level
- Repairability score
- Confidence indicator
- Suggested next step

### 3. Repair path screen

- DIY attempt
- Community helper
- Local repair event
- Parts donor / not worth repairing

### 4. Local community layer

- Nearby repair events
- Volunteer skill tags
- Category-specific support
- Estimated wait or availability

### 5. Outcome tracking

- Fixed successfully
- Partially fixed
- Could not be fixed
- Reused for parts
- Sent to recycling

### 6. Impact feedback

- Money saved estimate
- Waste avoided estimate
- Repair skills learned
- Community contribution history

## HCI Design Challenges

This concept creates several strong HCI questions that make it more than a generic app concept.

### Trust and explanation

Users may hesitate to follow an AI diagnosis unless the system explains why it gave a recommendation and how confident it is.[cite:149][cite:152]

### Anxiety and uncertainty

Users often fear making the object worse, spending money unnecessarily, or wasting time on an impossible repair. The interface should reduce uncertainty and support decision-making rather than overwhelm the user.

### Different knowledge levels

Beginners, hobbyists, and organizers need very different interfaces, information density, and decision support.

### Human-AI collaboration

The AI should support local repair communities, not replace them. The system must present AI as a guide that helps people reach better human-supported repair outcomes.[cite:118][cite:145][cite:147]

## Suggested MVP Scope for Figma

The initial prototype should focus on a realistic and presentable MVP rather than a full platform.

### Recommended MVP screens

1. Landing / home screen
2. Scan broken item screen
3. AI diagnosis result screen
4. Repair path recommendation screen
5. Local repair event / helper matching screen
6. Booking or help request screen
7. Repair outcome and impact screen

This scope is large enough for a 4-person team, but still focused enough to present clearly.

## Suggested Product Positioning

### Option A — AI-first

Focus on diagnosis quality, repairability scoring, and recommendation logic.

### Option B — Community-first

Focus on local volunteers, repair events, and support networks.

### Option C — Hybrid

Focus on the full journey from diagnosis to best repair pathway.

The strongest direction is the **hybrid** version, because it balances the AI novelty with the local-community dimension required by the course.[cite:118][cite:147][cite:153]

## Visual and Interaction Direction

The product should feel practical, optimistic, and trustworthy.

A good design direction would combine:
- simple mobile-first flows,
- clear diagnosis cards,
- transparency around AI confidence,
- visual indicators of repair difficulty,
- and community-oriented language that makes the experience feel approachable rather than technical.

The UI should avoid the feel of a cold service marketplace and instead emphasize learning, support, sustainability, and local participation.[cite:145][cite:153]

## Team Framing for a 4-Person Group

A practical split could be:

- **Member 1:** user research, personas, and problem framing
- **Member 2:** information architecture, task flows, and wireframes
- **Member 3:** UI system, visual design, and Figma prototyping
- **Member 4:** AI logic framing, feature definition, and presentation narrative

## Short Pitch

PatchUp is an AI-assisted repair platform for local communities that helps users understand whether a broken household item can be repaired, how difficult the repair may be, and which repair path makes the most sense: do it yourself, visit a repair event, or ask a local expert.[cite:146][cite:149][cite:152]

By combining AI diagnosis with community-based repair support, PatchUp encourages sustainable behavior, lowers the barrier to repair, and strengthens local repair ecosystems.[cite:118][cite:139][cite:153]

## One-Sentence Concept

**PatchUp is a mobile-first HCI concept for an AI-powered community repair platform that transforms a photo of a broken item into a clear repair decision and a locally actionable next step.**
