# Domain-classifier shift diagnostic: walkthrough

## 1. Pool the domains

Given source predictors X_s and target predictors X_t with the same feature columns, stack them into X and create a binary domain label y: zero for source and one for target.

## 2. Fit a classifier

Use a pipeline containing standardisation and logistic regression. The scaler is fitted only on each training fold, avoiding leakage from held-out rows.

## 3. Obtain out-of-fold probabilities

Stratified K-fold gives each row a held-out prediction. When meaningful spatial or temporal group labels are available, StratifiedGroupKFold keeps all rows from one group in a single fold. Groups should represent the independence/deployment units relevant to the task, not arbitrary row IDs.

## 4. Measure separability

Compute ROC AUC from out-of-fold target-domain probabilities. AUC of 0.5 corresponds to chance ranking; AUC near one means the fitted classifier distinguishes the sampled domains well. Balanced accuracy at a 0.5 probability threshold is also returned, but AUC is less tied to one threshold.

## 5. Interpretation

The diagnostic depends on the model class and features. It does not prove the distributions match when AUC is low, and it cannot identify concept shift from predictors alone. Spatial autocorrelation and sampling design still matter. Use it alongside MMD, energy distance, support diagnostics and deployment-matched validation.

## References

- Sugiyama, M., Krauledat, M. & Müller, K.-R. (2007). Covariate shift adaptation by importance weighted cross validation. Journal of Machine Learning Research, 8, 985–1005.
- Bickel, S., Brückner, M. & Scheffer, T. (2009). Discriminative learning under covariate shift. Journal of Machine Learning Research, 10, 2137–2155.
