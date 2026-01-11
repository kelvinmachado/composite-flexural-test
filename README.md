# Composite Flexural Test (ASTM D790)

Numerical model of the **ASTM D790 three-point bending test** for **laminated composite beams**, including **local contact and indentation effects** between rollers and the laminate.

---

## Description
The model combines:
- Classical Lamination Theory (CLT),
- equivalent beam formulation,
- simplified elastic contact at loading and support points.

It allows evaluating how **roller–laminate contact compliance** affects the load–displacement response and the apparent flexural properties obtained from the standard test.

---

## Features
- Arbitrary laminate stacking sequence.
- Orthotropic lamina properties.
- Explicit roller–laminate contact modeling.
- Load–displacement curve.
- ASTM D790 flexural modulus and maximum stress.
- Simple GUI for geometry, stacking sequence and material properties.

---

## Inputs
- Geometry: span, width, thickness.
- Lamina properties: \(E_1, E_2, G_{12}, \nu_{12}\).
- Stacking sequence.
- Roller radius and contact parameters.

---

## Outputs
- Load × displacement curve.
- Apparent flexural modulus.
- Maximum flexural stress.

---

## Limitations
- Linear elastic behavior.
- No damage or failure modeling.
- Three-point bending only.

---

## Purpose
Educational and exploratory tool for **composite mechanics and contact modeling**.