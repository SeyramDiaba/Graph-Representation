# Assignment 1: Graph Representation of Research Group
**Social Networks and Graph Analysis**  
**Student:** Stephen Diaba  
**Date:** November 14, 2025

---

## 1. Introduction

This report presents a network analysis of collaborative relationships within a research group. The objective is to model the group's structure as a graph, compute key network metrics, and visualize the relationships among members. The analysis was conducted using Python's NetworkX library for graph construction and analysis, and Matplotlib for visualization.

## 2. Methodology

### 2.1 Graph Construction

A simple undirected graph G = (V, E) was constructed where:
- **Nodes (V):** Represent individual members of the research group
- **Edges (E):** Represent collaborative relationships between members

The graph was implemented using the NetworkX library in Python. Nodes were added for each research group member, and edges were created based on collaborative relationships such as project work, supervision, and research partnerships.

### 2.2 Data Collection

The network consists of 12 members including faculty supervisors, research assistants, and students. Collaborative relationships were identified based on:
- Direct project collaboration
- Supervisory relationships
- Peer research partnerships

## 3. Results and Analysis

### 3.1 Basic Network Metrics

The analysis revealed the following fundamental characteristics of the research group network:

**Number of Nodes:** 12 members  
**Number of Edges:** 30 collaborative relationships

These metrics indicate a moderately connected research group with an average of 2.5 collaborations per edge, suggesting active engagement among members.

### 3.2 Degree Distribution

The degree distribution analysis shows the connectivity of each member:

| Member | Connections | Role |
|--------|-------------|------|
| Dr Ansah | 11 | Supervisor |
| Princilla | 10 | Research Assistant |
| Lydia | 4 | Student |
| Stephen | 3 | Student |
| Others | 1-2 | Various |

**Key Observations:**
- Dr Ansah exhibits the highest degree centrality (11 connections), connecting to all other members, consistent with a supervisory role
- Princilla serves as a secondary hub (10 connections), likely functioning as a project coordinator or senior research assistant
- Most students maintain 1-4 connections, indicating focused collaborative partnerships
- The degree distribution follows a typical hierarchical research group pattern

### 3.3 Isolated Nodes

Analysis using NetworkX's `isolates()` function revealed:

**Result:** No isolated nodes detected

This indicates that all members are integrated into the research group network. Every member has at least one collaborative relationship, suggesting good group cohesion and active participation.

### 3.4 Network Connectivity

The network demonstrates strong connectivity characteristics:
- All members are reachable from any other member through the collaboration network
- The presence of two high-degree nodes (Dr Ansah and Princilla) creates a resilient network structure
- Multiple pathways exist between most members, reducing dependency on single connections

## 4. Interpretation

### 4.1 Network Structure

The research group exhibits a **hub-and-spoke topology** with Dr Ansah as the central hub. This structure is typical in academic research groups where:
1. Faculty supervisors maintain connections with all students
2. Senior members (like Princilla) facilitate coordination
3. Students collaborate in smaller sub-groups

### 4.2 Collaboration Patterns

The network reveals several interesting patterns:
- **Hierarchical structure:** Clear distinction between supervisory and peer relationships
- **Secondary coordination:** Princilla's high connectivity suggests an important coordinating role
- **Peer clusters:** Groups like (Stephen-Phillip), (Daniel-Prince), and (Samuel-Charles) indicate focused project teams
- **Bridge connections:** Members like Lydia connect multiple sub-groups

### 4.3 Network Health

The absence of isolated nodes indicates:
- Effective integration of all members
- Active collaboration culture
- Successful group management
- No marginalized members requiring intervention

## 5. Visualization

The network visualization (see `network.png`) illustrates:
- Node size proportional to connections
- Clear identification of hub members
- Spatial clustering of closely connected members
- Overall network topology

The spring layout algorithm positions highly connected nodes centrally, making the hierarchical structure visually apparent.

## 6. Conclusions

This analysis successfully modeled the research group as a network graph and computed essential metrics. Key findings include:

1. **Well-connected group:** 12 members with 30 collaborations demonstrate active engagement
2. **Clear leadership structure:** Dr Ansah's central position reflects supervisory responsibilities
3. **No isolation:** All members participate in collaborative relationships
4. **Balanced distribution:** Mix of strong hub connections and peer-to-peer collaborations

The network structure appears healthy and conducive to collaborative research. The presence of multiple high-degree nodes provides redundancy, while peer-to-peer connections foster independent collaboration beyond direct supervision.

### Future Considerations

For continued network health, the group might consider:
- Encouraging more cross-cluster collaborations
- Mentoring new members through multiple connections
- Maintaining the current balance between hierarchical and peer relationships

---

## 7. Technical Implementation

**Tools Used:**
- Python 3.x
- NetworkX 3.x (graph construction and analysis)
- Matplotlib (visualization)

**Deliverables:**
1. Python source code: `Assignment1.py`
2. Network visualization: `network.png`
3. Gephi-compatible file: `research_group.gexf`
4. This report: `Assignment1_Report.pdf`

**Code Repository:** Available on GitHub at the course assignment repository

---

## References

NetworkX Documentation. (2025). NetworkX - Network Analysis in Python. Retrieved from https://networkx.org/

Barabási, A. L. (2016). *Network Science*. Cambridge University Press.
