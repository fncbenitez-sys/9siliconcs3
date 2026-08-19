# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Francis Nicholai C. Benitez
**Section:** 9-Silicon
**Last Name:** Benitez
**Date:** 8/16/2026
---

## Step 1: Identify the Big Problem
### Main Problem
The canteen service pipeline is inefficient and bottlenecked by manual ordering, slow cash-handling transactions, and unmonitored food inventory during peak lunch hours.
---
## Step 2: Identify the Sub-Problems
1. Ordering Delay: Students spend excess time deliberating choices at the service counter rather than beforehand.
2. Payment Bottleneck: Cashiers manually total order prices, compute change, and handle cash transactions during checkout.
3. Inventory Blindspot: Lack of real-time stock tracking causes unexpected item stock-outs during ordering.
4. Queue Management: Absence of an organized queuing structure or digital ticket notification causes physical crowding.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |

| Ordering Delay      | Abstraction         | Display a simplified digital menu board outside the queue showing only item names, prices, and live availability so students decide before reaching the counter.         |

| Payment Bottleneck  | Algorithm Design    | Implement a Point-of-Sale (POS) or pre-loaded RFID ID card scanner that automatically calculates total cost, deducts balance, and computes change instantaneously.  |

| Inventory Blindspot | Pattern Recognition | Analyze historical sales data across weekdays to identify high-demand items and set auto-alerts when inventory drops below a 10-unit threshold.                   |

| Queue Management    | Decomposition       | Break the queue lifecycle into distinct sub-processes: Order Entry > Automated Billing > Queue Number Generation > Meal Pickup.                                        |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Payment Bottleneck
### Pseudocode
START 
START
Display total order cost
Input RFID card scan or payment details
Check if card balance >= total order cost
IF balance is sufficient THEN
    Deduct total order cost from balance
    Calculate remaining balance
    Display payment success, receipt, and remaining balance
ELSE
    Display "Insufficient Balance" error
END
---