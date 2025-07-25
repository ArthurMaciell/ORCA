from ORCA.utils.common import get_size
from ORCA import logger
import os
import urllib.request as request
import zipfile
from pathlib import Path
from ORCA.entity.config_entity import (DataTransformationConfig)
from sklearn.model_selection import train_test_split
import pandas as pd
from typing import Tuple, List
import numpy as np

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

    def prepare_dataframe(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, List[str], List[str]]:
        # Filtrar apenas os modelos "AR"
        df = df[df['Modelo'] == 'AR'].copy()

        # Converter Data
        df['Data'] = pd.to_datetime(df['Data'], format="%d/%m/%Y")

        # Calcular Área
        df["Area"] = df["Comprimento"] * df["Largura"]
        df["Area"] = df["Area"].replace([np.inf, -np.inf], np.nan)
        df["AreaAusente"] = df["Area"].isna()
        df["Area"] = df["Area"].fillna(0)

        # Converter Preço Unitário e Fator
        df['Preço Unitário'] = pd.to_numeric(df['Preço Unitário'], errors='coerce')
        df['Fator'] = pd.to_numeric(df['Fator'], errors='coerce')
        df['Preco (1)'] = df['Preço Unitário'] / df['Fator']

        # Ajuste de preço por ano
        df.loc[df['Data'].dt.year == 2022, 'Preco (1)'] *= 1.20
        df.loc[df['Data'].dt.year == 2023, 'Preco (1)'] *= 1.10
        df.loc[df['Data'].dt.year == 2024, 'Preco (1)'] *= 1.15

        # Categorizar preços
        q1 = df['Preco (1)'].quantile(0.33)
        q2 = df['Preco (1)'].quantile(0.66)

        def categorize_price(price):
            if price <= q1:
                return 'Low'
            elif price <= q2:
                return 'Medium'
            else:
                return 'High'

        df['preco_categoria'] = df['Preco (1)'].apply(categorize_price)

        # Comprimento / Largura
        df["Comprimento/Largura"] = df["Comprimento"] / df["Largura"].replace(0, np.nan)
        df["Comprimento/Largura"] = df["Comprimento/Largura"].fillna(0)

        # Limpar colunas desnecessárias
        primeira_coluna = df.columns[0]
        df = df.drop(columns=[primeira_coluna])

        # Remover linhas sem modelo
        df = df[df['Modelo'].notna() & (df['Modelo'] != '')]

        # Remover colunas completamente vazias
        colunas_vazias = df.columns[df.isna().all()].tolist()
        colunas_tirar = ['Descricao', 'Linha', 'Data', 'Qnt', 'Fator', 'Total', 'Peso', 'Volume', 'Preço Unitário']
        df = df.drop(columns=colunas_vazias + colunas_tirar, errors='ignore')

        # Tratar valores ausentes
        colunas_numericas = ['Comprimento', 'Largura']
        df[colunas_numericas] = df[colunas_numericas].fillna(0)

        colunas_categoricas = df.select_dtypes(include='object').columns.tolist()
        df[colunas_categoricas] = df[colunas_categoricas].fillna("Ausente")

        if 'Moldura' in df.columns:
            df['Moldura'] = df['Moldura'].fillna("Ausente")

        # Remover duplicadas
        df_encoded = pd.get_dummies(df)
        df_encoded = df_encoded.drop_duplicates()
        
        logger.info(f"DataFrame preparado com shape: {df.shape} | Codificado: {df_encoded.shape}")


        return df, df_encoded, colunas_numericas, colunas_categoricas
        
    def train_test_spliting(self):
        df = pd.read_excel(self.config.data_input_path)
        df_ar, df_encoded_ar, _, _ = self.prepare_dataframe(df)
        
        # Salvar o dataframe codificado completo
        df_encoded_ar.to_excel(self.config.transformed_data_path, index=False)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(df_encoded_ar, test_size=0.2, random_state=42)

        train.to_excel(os.path.join(self.config.root_dir, "train.xlsx"),index = False)
        test.to_excel(os.path.join(self.config.root_dir, "test.xlsx"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        
    def save_encoded_dataframe(self, df_encoded: pd.DataFrame):
        os.makedirs(self.config.root_dir, exist_ok=True)
        df_encoded.to_excel(self.config.transformed_data_path, index=False)
        logger.info(f"Arquivo codificado salvo em: {self.config.transformed_data_path}")
        