from engineProject.entity.config_entity import DataCleaningConfig
import pandas as pd
import os

class DataCleaning:
    def __init__(self, config: DataCleaningConfig):
        self.config = config


    def cleaned_data(self) -> pd.DataFrame:
      
        df = pd.read_csv(self.config.unzip_data_dir)

        
        df= df.sample(frac=1)
        maintenance_df = df.loc[df['Engine Condition'] == 1][:7218]
        great_df = df.loc[df['Engine Condition'] == 0]

        new_df = pd.concat([maintenance_df, great_df])

        new_df = df.sample(frac=1, random_state=42)

        save_path = os.path.join(self.config.root_dir, "new_df.csv")
        new_df.to_csv(save_path, index=False)

        return new_df