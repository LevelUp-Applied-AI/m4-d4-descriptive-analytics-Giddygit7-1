"""Core Skills Drill — Descriptive Analytics

Compute summary statistics, plot distributions, and create a correlation
heatmap for the sample sales dataset.

Usage:
    python drill_eda.py
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def compute_summary(df):
    summary = df.describe()
    summary.loc['median'] = df.median(numeric_only=True)
    summary = summary.loc[['count', 'mean', 'median', 'std', 'min', 'max']]
    summary.to_csv('output/summary.csv')
    return summary


def compute_summary(df):
    summary = df.describe()
    summary.loc['median'] = df.median(numeric_only=True)
    summary = summary.loc[['count', 'mean', 'median', 'std', 'min', 'max']]
    summary.to_csv('output/summary.csv')
    return summary

def plot_distributions(df, columns, output_path):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()
    for i, col in enumerate(columns):
        sns.histplot(df[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Dist of {col}')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_correlation(df, output_path):
    corr_matrix = df.select_dtypes(include='number').corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main():
    os.makedirs("output", exist_ok=True)
    df = pd.read_csv('data/sample_sales.csv')
    
    if 'unit_price' in df.columns and 'quantity' in df.columns:
        df['revenue'] = df['unit_price'] * df['quantity']
    
    compute_summary(df)
    
    cols_to_plot = ['unit_price', 'quantity', 'revenue', 'quantity']
    plot_distributions(df, cols_to_plot, 'output/distributions.png')
    
    plot_correlation(df, 'output/correlation.png')

if __name__ == "__main__":
    main()
