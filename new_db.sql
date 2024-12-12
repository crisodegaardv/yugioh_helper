CREATE TABLE "card"(
    "id" INT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,  -- Changed to TEXT for flexibility
    PRIMARY KEY("id")
);

CREATE TABLE "card_type"(
    "id" INT NOT NULL,
    "card_type_name" VARCHAR(255) NOT NULL,  -- Renamed to a more descriptive name
    PRIMARY KEY("id")
);

CREATE TABLE "card_card_type"(
    "card_id" INT NOT NULL,
    "card_type_id" INT NOT NULL,
    PRIMARY KEY("card_id", "card_type_id")  -- Composite primary key
);

ALTER TABLE "card_card_type" 
    ADD CONSTRAINT "card_card_type_card_id_foreign" 
    FOREIGN KEY("card_id") REFERENCES "card"("id");

ALTER TABLE "card_card_type" 
    ADD CONSTRAINT "card_card_type_card_type_id_foreign" 
    FOREIGN KEY("card_type_id") REFERENCES "card_type"("id");

-- Optional: Create indexes for better performance in case of frequent queries
CREATE INDEX idx_card_id ON "card_card_type"("card_id");
CREATE INDEX idx_card_type_id ON "card_card_type"("card_type_id");
