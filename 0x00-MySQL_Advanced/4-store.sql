-- script that creates a trigger that decreases the quantity of an item 
-- after adding a new order.
CREATE TRIGGER decrease_qty_after_new_order
AFTER INSERT ON orders FOR EACH ROW
UPDATE TABLE items SET quantity = quantity - NEW.number
WHERE name = NEW.items_name;