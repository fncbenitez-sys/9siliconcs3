## 1. Encapsulation
Encapsulation binds together data properties and the methods that operate on them into a single Product unit, while restricting direct access to the underlying variables. In a sari-sari store system, properties like name, price, and quantity are kept private so that external code cannot modify stock levels or costs directly. Instead, operations occur strictly through public methods like update_stock() or apply_discount(), which enforce rules such as preventing negative inventory. This prevents unexpected data corruption and ensures that all changes to product state follow consistent validation logic.


## 2. Abstraction
Abstraction hides the internal, complex implementation details of system operations and exposes only essential features to the rest of the application. An InventoryManager class can provide clean, high-level methods like sell_item() or generate_daily_report() without exposing how stock values are recalculated or how reports are formatted. The store manager or checkout interface interacts only with simple function calls, unconcerned with the underlying database or algorithmic steps. This simplifies overall program design by reducing dependencies and allowing internal mechanics to be upgraded without breaking user-facing functions.


## 3. Inheritance
Inheritance allows specialized child classes to derive shared attributes and behaviors from a general parent class. A base Product class can define core properties like name, price, and quantity, which are then inherited by sub-classes such as PerishableProduct (adding expiration_date) or Beverage (adding is_chilled or volume). This structure eliminates redundant code definitions across different product categories within the store. It optimizes program organization by creating a logical hierarchy and allowing shared functionality to be maintained in a single place.


## 4. Polymorphism
Polymorphism enables objects of different specialized classes to respond to the same method call in unique ways. A parent Product class might declare a calculate_final_price() method, which is overridden by PerishableProduct to automatically apply a markdown as the expiration date approaches, or by BulkProduct to apply volume discounts. The inventory system can iterate through a master list of generic products and trigger calculate_final_price() without needing separate conditional logic for every item type. This design flexible and easy to extend when introducing new product types to the inventory.




### Reflection
Encapsulation would be the most critical pillar for improving the sari-sari store inventory system. By bundling properties like price and quantity with valid methods to modify them, it directly solves the issue of data instability inherent in procedural code using loose global variables. It guarantees that inventory counts cannot accidentally drop below zero or undergo unauthorized price edits from external functions. This fundamental layer of data protection establishes a reliable foundation, ensuring accurate records before scaling the system with features like inheritance or polymorphism.