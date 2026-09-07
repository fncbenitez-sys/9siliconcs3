# SG4 - Understanding Classes and Objects
## Student
## This class represents students as they're being checked for dresscode or grooming infractions.

## Properties
|  Property  | Data Type |             Description            |
|------------|-----------|------------------------------------|
|Hair Color  | Boolean   |If hair color is natural            |
|Hair Length | Boolean   |If hair length is appropriate       |
|Cut Nails   | Boolean   |If nails are cut                    |
|Uniform     | Boolean   |If in complete uniform              |

## Methods
| Method |                        Description                       |
|--------|----------------------------------------------------------|
|Offense |Offends the student if there are more than 2 false values |
|Warn    |Warns the student if there is 1 false value               |
|Ignore  |Ignores the student if there are no false values          |

## Class Diagram
![Class Diagram Part 1](q1\images\classDiagram1.png), [Class Diagram Part 2](q1\images\classDiagram2.png)
## Design Explanation
### Why did you choose this class?
###     > To help people check if they're in violation of the code of conduct
### Which property is the most important? Why?
###     > Hair color, it is one of the most obvious and easy to notice property of the human student.
### Which method is the most useful? Why?
###     > Warn, it tells the student that they could be violated next time if they don't change their [enter violated property here]