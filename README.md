# RISC-V Custom Assembler & Simulator

> A complete 32-bit RISC-V-like ISA implementation — from human-readable assembly to binary execution.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-RISC--V%2032--bit-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20WSL-informational?style=flat-square&logo=linux&logoColor=white)

---
## Overview

This project implements a custom **32-bit RISC-V-like Instruction Set Architecture** consisting of two core components:

- **Assembler** — translates `.txt` assembly source files into 32-bit binary machine code
- **Simulator** — executes that binary on a virtual CPU, maintaining full register and memory state

Built with automated testing at its core, the entire pipeline can be validated against golden reference outputs using the included test suite.

---

## Features

| Feature | Details |
|---|---|
| **Two-Pass Assembler** | Handles labels, forward references, and full instruction encoding |
| **ISA Coverage** | R, I, S, B, U, and J type instruction formats |
| **Simulator Engine** | Tracks PC, 32 general-purpose registers, and memory state |
| **Bonus Instructions** | `mul`, `rst`, `halt`, `rvrs` |
| **Error Reporting** | Line-precise syntax errors, optimized for the ErrorGen test suite |
| **Automated Testing** | Full integration framework with golden file comparison |

---

## Project Structure

```
.
├── Assembler.py          # Translates .txt assembly into 32-bit binary strings
├── Simulator.py          # Virtual CPU — executes binary and maintains system state
└── automatedTesting/     # Test framework for validating assembler & simulator output
    └── src/
        └── main.py
```

---

## Getting Started

### Prerequisites

> ⚠️ The automated test infrastructure requires a **Linux-based shell**.  
> **Windows users** must use [WSL](https://learn.microsoft.com/en-us/windows/wsl/) or a Virtual Machine.

- Python 3.8+

### Running the Test Suite

Navigate into the `automatedTesting/` directory first:

```bash
cd automatedTesting
```

**Test Assembler only:**
```bash
python3 src/main.py --no-sim --linux
```

**Test Simulator only:**
```bash
python3 src/main.py --no-asm --linux
```

**Run full pipeline (Assembler + Simulator):**
```bash
python3 src/main.py --linux
```

---

## Implementation Details

### Assembler

- **Two-pass design** resolves all labels and forward references before encoding
- **B-Type / J-Type instructions** implement RISC-V's bit-shuffling logic for scrambled immediates
- **Memory addressing** includes a dedicated parser for `offset(register)` syntax used in `lw` / `sw`
- **Input cleaning** strips commas and normalizes whitespace before processing

### Simulator

Replicates the standard **Fetch → Decode → Execute** cycle:

```
Fetch    →  Load 32-bit instruction from memory at PC
Decode   →  Extract opcode, funct3, funct7, and register fields
Execute  →  Perform ALU operation or memory access
Update   →  Log register trace and advance the Program Counter
```


---
## Team

| Name | 
|---|
| Hemant Meena |
| Dev Chaudhary |
| Piyush |
| Aditya Singh |

---

> *CO Assignment — Computer Organization*
