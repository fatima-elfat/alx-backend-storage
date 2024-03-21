-- Task 4: Buy buy buy.
DELIMITER //
CREATE TRIGGER buy_trigger
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
//
DELIMITER ;