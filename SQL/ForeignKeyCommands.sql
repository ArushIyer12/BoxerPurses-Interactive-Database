ALTER
TABLE [dbo].Bouts
ADD CONSTRAINT FK_Venue_ID_2 FOREIGN KEY (Venue_ID)
REFERENCES [dbo].Venues (Venue_ID);

ALTER
TABLE [dbo].Bouts
ADD CONSTRAINT FK_production_ID_2 FOREIGN KEY (Production_ID)
REFERENCES [dbo].Productions (Production_ID);

ALTER
TABLE [dbo].Bouts
ADD CONSTRAINT FK_promotional_ID_2 FOREIGN KEY (Promotional_ID)
REFERENCES [dbo].Promotions(Promotional_ID);

ALTER
TABLE [dbo].Bouts
ADD CONSTRAINT FK_boxer_ID_2 FOREIGN KEY (Boxer_ID)
REFERENCES [dbo].Boxers(Boxer_ID);

ALTER
TABLE [dbo].Bouts
ADD CONSTRAINT FK_weight_ID_2 FOREIGN KEY (Weight_ID)
REFERENCES [dbo].Weights(Weight_class_ID);

ALTER
TABLE [dbo].Bouts
ADD CONSTRAINT FK_fight_importance_ID_2 FOREIGN KEY (Fight_Importance_ID)
REFERENCES [dbo].Importances(Importance_ID);








