feature_importances = pd.DataFrame({"features": rf_best.feature_names_in_, "importance": rf_best.feature_importances_}).sort_values("importance",ascending = False)
feature_importances.sort_values('importance',ascending=False,inplace=True)
sns.barplot(data=feature_importances,x='importance',y='features',palette='viridis')
plt.title('RandomForest base on train data (best model)')