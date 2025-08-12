# FDE Technical Screen - Package Sorting Solution

## 🎯 **Challenge Overview**

**Company**: Thoughtful Automation  
**Position**: Software Engineer  
**Challenge**: Robotic Factory Package Sorting Algorithm  
**Time Limit**: 30 minutes  
**Language**: Python (Required)  

## 📋 **Problem Statement**

Implement a function for a robotic arm that dispatches packages to the correct stack according to their volume and mass.

### **Classification Rules:**
- **BULKY**: Volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- **HEAVY**: Mass ≥ 20 kg

### **Stack Assignments:**
- **STANDARD**: Neither bulky nor heavy packages
- **SPECIAL**: Packages that are either heavy OR bulky (but not both)
- **REJECTED**: Packages that are BOTH heavy AND bulky
