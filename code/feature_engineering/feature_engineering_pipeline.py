"""
Feature Engineering Pipeline
=============================

Comprehensive feature engineering examples for machine learning.

Topics covered:
- Missing value imputation
- Categorical encoding
- Feature scaling and transformation
- Feature creation and interaction terms
- Dimensionality reduction
- Feature selection
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif
from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from typing import List, Tuple
import warnings
warnings.filterwarnings('ignore')

sns.set_style("whitegrid")


class FeatureEngineeringPipeline:
    """
    Comprehensive feature engineering pipeline.

    Parameters
    ----------
    numerical_features : list
        Names of numerical features
    categorical_features : list
        Names of categorical features
    target : str
        Target variable name
    """

    def __init__(self, numerical_features: List[str],
                 categorical_features: List[str],
                 target: str = 'target'):
        self.numerical_features = numerical_features
        self.categorical_features = categorical_features
        self.target = target
        self.pipeline = None
        self.feature_names = None

    def create_basic_pipeline(self, strategy: str = 'robust') -> ColumnTransformer:
        """
        Create a basic preprocessing pipeline.

        Parameters
        ----------
        strategy : str
            Scaling strategy: 'standard', 'minmax', or 'robust'

        Returns
        -------
        ColumnTransformer
            Preprocessing pipeline
        """
        # Numerical pipeline
        if strategy == 'standard':
            scaler = StandardScaler()
        elif strategy == 'minmax':
            scaler = MinMaxScaler()
        else:
            scaler = RobustScaler()

        numerical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', scaler)
        ])

        # Categorical pipeline
        categorical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(drop='first', sparse_output=False,
                                     handle_unknown='ignore'))
        ])

        # Combine pipelines
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_pipeline, self.numerical_features),
                ('cat', categorical_pipeline, self.categorical_features)
            ],
            remainder='passthrough'
        )

        self.pipeline = preprocessor
        return preprocessor

    def create_polynomial_features(self, df: pd.DataFrame, degree: int = 2,
                                   interaction_only: bool = False) -> pd.DataFrame:
        """
        Create polynomial and interaction features.

        Parameters
        ----------
        df : pd.DataFrame
            Input dataframe
        degree : int
            Polynomial degree
        interaction_only : bool
            Only create interaction terms (no powers)

        Returns
        -------
        pd.DataFrame
            DataFrame with polynomial features
        """
        from sklearn.preprocessing import PolynomialFeatures

        poly = PolynomialFeatures(degree=degree,
                                 interaction_only=interaction_only,
                                 include_bias=False)

        num_data = df[self.numerical_features].values
        poly_features = poly.fit_transform(num_data)

        # Create feature names
        feature_names = poly.get_feature_names_out(self.numerical_features)

        poly_df = pd.DataFrame(poly_features, columns=feature_names,
                              index=df.index)

        # Combine with categorical features
        if self.categorical_features:
            result = pd.concat([poly_df, df[self.categorical_features]], axis=1)
        else:
            result = poly_df

        return result

    def create_domain_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create domain-specific features (example for demo).

        Parameters
        ----------
        df : pd.DataFrame
            Input dataframe

        Returns
        -------
        pd.DataFrame
            DataFrame with new features
        """
        df_new = df.copy()

        # Example: ratio features
        if len(self.numerical_features) >= 2:
            f1, f2 = self.numerical_features[0], self.numerical_features[1]
            df_new[f'{f1}_to_{f2}_ratio'] = df_new[f1] / (df_new[f2] + 1e-8)

        # Example: binning
        if len(self.numerical_features) >= 1:
            f = self.numerical_features[0]
            df_new[f'{f}_binned'] = pd.cut(df_new[f], bins=5,
                                          labels=['very_low', 'low', 'medium',
                                                 'high', 'very_high'])

        return df_new

    def select_features_univariate(self, X: pd.DataFrame, y: pd.Series,
                                   k: int = 10) -> List[str]:
        """
        Select top k features using univariate statistical tests.

        Parameters
        ----------
        X : pd.DataFrame
            Feature matrix
        y : pd.Series
            Target variable
        k : int
            Number of features to select

        Returns
        -------
        list
            Selected feature names
        """
        # Ensure numerical data only
        X_num = X.select_dtypes(include=[np.number])

        selector = SelectKBest(f_classif, k=min(k, X_num.shape[1]))
        selector.fit(X_num, y)

        # Get selected feature names
        selected_mask = selector.get_support()
        selected_features = X_num.columns[selected_mask].tolist()

        # Get scores
        scores = pd.DataFrame({
            'feature': X_num.columns,
            'score': selector.scores_
        }).sort_values('score', ascending=False)

        print("\nTop 10 features by F-score:")
        print(scores.head(10))

        return selected_features

    def select_features_rfe(self, X: pd.DataFrame, y: pd.Series,
                           n_features: int = 10) -> List[str]:
        """
        Recursive Feature Elimination using Random Forest.

        Parameters
        ----------
        X : pd.DataFrame
            Feature matrix
        y : pd.Series
            Target variable
        n_features : int
            Number of features to select

        Returns
        -------
        list
            Selected feature names
        """
        X_num = X.select_dtypes(include=[np.number])

        estimator = RandomForestClassifier(n_estimators=100, random_state=42)
        selector = RFE(estimator, n_features_to_select=n_features, step=1)
        selector.fit(X_num, y)

        selected_mask = selector.get_support()
        selected_features = X_num.columns[selected_mask].tolist()

        # Show ranking
        ranking = pd.DataFrame({
            'feature': X_num.columns,
            'ranking': selector.ranking_
        }).sort_values('ranking')

        print("\nFeature rankings (1 = selected):")
        print(ranking.head(15))

        return selected_features

    def dimensionality_reduction_pca(self, X: pd.DataFrame,
                                    n_components: int = 2,
                                    plot: bool = True) -> Tuple[np.ndarray, PCA]:
        """
        Apply PCA for dimensionality reduction.

        Parameters
        ----------
        X : pd.DataFrame
            Feature matrix
        n_components : int
            Number of principal components
        plot : bool
            Whether to plot explained variance

        Returns
        -------
        tuple
            (Transformed data, fitted PCA object)
        """
        X_num = X.select_dtypes(include=[np.number])

        # Standardize first
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_num)

        # Apply PCA
        pca = PCA(n_components=n_components)
        X_pca = pca.fit_transform(X_scaled)

        if plot:
            fig, axes = plt.subplots(1, 2, figsize=(14, 5))

            # Explained variance
            axes[0].bar(range(1, n_components + 1),
                       pca.explained_variance_ratio_)
            axes[0].set_xlabel('Principal Component')
            axes[0].set_ylabel('Explained Variance Ratio')
            axes[0].set_title('PCA Explained Variance')

            # Cumulative variance
            cumvar = np.cumsum(pca.explained_variance_ratio_)
            axes[1].plot(range(1, n_components + 1), cumvar, 'o-')
            axes[1].set_xlabel('Number of Components')
            axes[1].set_ylabel('Cumulative Explained Variance')
            axes[1].set_title('Cumulative Explained Variance')
            axes[1].axhline(y=0.95, color='r', linestyle='--',
                          label='95% variance')
            axes[1].legend()

            plt.tight_layout()
            plt.savefig('pca_analysis.png', dpi=150, bbox_inches='tight')
            plt.show()

        print(f"\nExplained variance ratio: {pca.explained_variance_ratio_}")
        print(f"Total variance explained: {pca.explained_variance_ratio_.sum():.2%}")

        return X_pca, pca


def demonstrate_missing_values():
    """Demonstrate different missing value imputation strategies."""
    print("=" * 70)
    print("Missing Value Imputation Strategies")
    print("=" * 70)

    np.random.seed(42)
    n = 1000

    # Create data with missing values
    df = pd.DataFrame({
        'age': np.random.normal(40, 15, n),
        'income': np.random.lognormal(10, 1, n),
        'score': np.random.normal(70, 15, n)
    })

    # Introduce missing values
    missing_mask = np.random.random(n) < 0.2
    df.loc[missing_mask, 'income'] = np.nan

    print(f"\nMissing values: {df.isnull().sum()['income']} / {n}")

    # Different imputation strategies
    strategies = {
        'Mean': SimpleImputer(strategy='mean'),
        'Median': SimpleImputer(strategy='median'),
        'KNN': KNNImputer(n_neighbors=5)
    }

    results = {}
    for name, imputer in strategies.items():
        df_imputed = df.copy()
        df_imputed[['income']] = imputer.fit_transform(df[['income']])
        results[name] = df_imputed['income']

    # Plot comparison
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))

    # Original data (before introducing missing values)
    true_income = np.random.lognormal(10, 1, n)
    axes[0].hist(true_income[missing_mask], bins=30, alpha=0.7, color='gray')
    axes[0].set_title('True Values\n(before missing)')
    axes[0].set_xlabel('Income')

    for idx, (name, imputed) in enumerate(results.items(), 1):
        axes[idx].hist(imputed[missing_mask], bins=30, alpha=0.7)
        axes[idx].set_title(f'{name} Imputation')
        axes[idx].set_xlabel('Income')

    plt.tight_layout()
    plt.savefig('imputation_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()


def demonstrate_encoding():
    """Demonstrate categorical encoding strategies."""
    print("\n" + "=" * 70)
    print("Categorical Encoding Strategies")
    print("=" * 70)

    # Sample data
    df = pd.DataFrame({
        'city': ['NYC', 'LA', 'Chicago', 'NYC', 'LA'] * 20,
        'education': ['HS', 'BS', 'MS', 'PhD', 'BS'] * 20,
        'salary': np.random.normal(70000, 20000, 100)
    })

    print("\nOriginal data sample:")
    print(df.head())

    # 1. Label Encoding
    le = LabelEncoder()
    df['city_label'] = le.fit_transform(df['city'])

    # 2. One-Hot Encoding
    df_onehot = pd.get_dummies(df, columns=['city', 'education'],
                               prefix=['city', 'edu'], drop_first=True)

    # 3. Ordinal Encoding (for education)
    education_order = ['HS', 'BS', 'MS', 'PhD']
    ordinal_encoder = OrdinalEncoder(categories=[education_order])
    df['education_ordinal'] = ordinal_encoder.fit_transform(df[['education']])

    # 4. Target Encoding (mean encoding)
    city_means = df.groupby('city')['salary'].mean()
    df['city_target_encoded'] = df['city'].map(city_means)

    print("\nEncoding results:")
    print(f"Label encoding: {df[['city', 'city_label']].head()}")
    print(f"\nOne-hot encoding columns: {[c for c in df_onehot.columns if 'city_' in c or 'edu_' in c]}")
    print(f"\nOrdinal encoding: {df[['education', 'education_ordinal']].head()}")
    print(f"\nTarget encoding: {df[['city', 'city_target_encoded']].head()}")


def demonstrate_complete_pipeline():
    """Demonstrate a complete feature engineering pipeline."""
    print("\n" + "=" * 70)
    print("Complete Feature Engineering Pipeline")
    print("=" * 70)

    # Load or create sample data
    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=1000, n_features=20, n_informative=10,
                               n_redundant=5, n_classes=2, random_state=42)

    # Create DataFrame
    feature_names = [f'feature_{i}' for i in range(20)]
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y

    # Add some categorical features
    df['category_A'] = np.random.choice(['cat1', 'cat2', 'cat3'], 1000)
    df['category_B'] = np.random.choice(['low', 'medium', 'high'], 1000)

    # Introduce missing values
    for col in feature_names[:5]:
        mask = np.random.random(1000) < 0.1
        df.loc[mask, col] = np.nan

    print(f"\nDataset shape: {df.shape}")
    print(f"Missing values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop('target', axis=1), df['target'],
        test_size=0.2, random_state=42
    )

    # Create pipeline
    numerical_features = feature_names
    categorical_features = ['category_A', 'category_B']

    fe = FeatureEngineeringPipeline(numerical_features, categorical_features)

    # Build and apply pipeline
    preprocessor = fe.create_basic_pipeline(strategy='robust')
    X_train_transformed = preprocessor.fit_transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)

    print(f"\nTransformed data shape: {X_train_transformed.shape}")

    # Feature selection
    X_train_df = pd.DataFrame(X_train_transformed,
                             columns=range(X_train_transformed.shape[1]))
    selected_features = fe.select_features_univariate(X_train_df, y_train, k=10)

    # Train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train_transformed, y_train)

    # Feature importance
    importances = pd.DataFrame({
        'feature': range(len(clf.feature_importances_)),
        'importance': clf.feature_importances_
    }).sort_values('importance', ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(range(15), importances.head(15)['importance'])
    plt.xlabel('Feature Index')
    plt.ylabel('Importance')
    plt.title('Top 15 Feature Importances')
    plt.tight_layout()
    plt.savefig('feature_importance.png', dpi=150, bbox_inches='tight')
    plt.show()

    print("\nTop 10 most important features:")
    print(importances.head(10))

    # Model performance
    from sklearn.metrics import classification_report
    y_pred = clf.predict(X_test_transformed)
    print("\nModel Performance:")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    demonstrate_missing_values()
    demonstrate_encoding()
    demonstrate_complete_pipeline()

    print("\nAll feature engineering examples completed!")
