# GeoAI foundations exercises

These exercises connect the [GeoAI foundations path](../learning-paths/geoai-foundations.md), [contrastive learning lesson](../algorithms/geoai/contrastive-info-nce.md), [masked autoencoding lesson](../methods/masked-autoencoding.md) and [spatial cross-validation lesson](../methods/spatial-cross-validation.md).

## 1. Choose the representation target

Choose one task: land-cover mapping, road extraction, crop-type classification, building change detection or flood mapping.

- Define the spatial unit represented by one token.
- List the sensor bands, acquisition dates, spatial resolution and quality masks needed.
- State what information a useful embedding must preserve.
- Identify one property that should not be treated as invariant.

## 2. Compare self-supervised objectives

- Explain what makes a positive pair in NT-Xent.
- Explain what is reconstructed in masked autoencoding.
- Identify a likely false-negative problem in contrastive learning.
- Identify a reconstruction shortcut that could produce low MAE loss but poor downstream representations.
- State what additional objective or evaluation could expose each failure.

## 3. Inspect patch masking

Run the [masked-autoencoding example](../implementations/python/masked-autoencoding/README.md).

- Change the mask ratio and count visible patches.
- Confirm that restore_indices returns visible tokens to their original sequence positions.
- Implement a temporal sequence with a shared spatial mask across dates.
- Compare it with independently masked dates.
- Explain which strategy may better support temporal change understanding and why.

## 4. Design a spatial evaluation

Use the [spatial cross-validation implementation](../implementations/python/spatial-cross-validation/README.md).

- Create a synthetic set of overlapping image tile centres.
- Compare a random row split with grid-block folds.
- Add a distance buffer and report the excluded observations.
- Explain why a reproducible seed does not make the split scientifically appropriate.
- Propose a separate held-out region and time period for a transfer test.

## 5. Design a model comparison

Plan a fair comparison between a random-initialised encoder, a supervised baseline, a contrastive model and a masked-autoencoder model.

- Fix the training geography and data period.
- Use the same downstream labels and test geography.
- Compare frozen linear probes and fine-tuning under the same label budget.
- Report class-wise metrics, uncertainty, geographic performance gaps and compute costs.
- State what result would make you reject the foundation-model approach for this task.

## 6. Research a named model responsibly

Choose SatMAE or Scale-MAE.

- Find the original paper and official project repository.
- Record the publication venue, data sources, sensor/modalities, pretraining objective and licence.
- Separate what the authors actually evaluated from what you hope the model can do.
- Do not infer that a model is suitable for a new region or sensor without a transfer test.

## Submission

Submit a short experiment plan, split diagram, augmentation/masking rationale, model comparison table and a limitations section. A model name or a lower pretraining loss is not a result by itself.
