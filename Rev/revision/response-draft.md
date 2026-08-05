# Response to reviewers and editors of manuscript number MLD01e1

Note: All the line numbers and page numbers are in the version without markup.

# Revision Summary

We thank the editor and reviewers for their careful and constructive comments. We hereby resubmit a revised version of our manuscript that addresses all points raised.

The main revisions are summarized below:

- We clarify the study design and analytical framework in the Abstract and Introduction, report key quantitative findings, incorporate the suggested literature, and sharpen the research gaps and objectives.
- We refine the study’s theoretical contribution by presenting education as an upstream component of climate-related cognitive and behavioral pathways while avoiding unsupported novelty and causal claims.
- We expand the Methodology to explain survey-wave pooling, model inputs and validation, gain-based feature importance, cross-layer prediction, model-based effect estimation, and the associated assumptions and limitations.
- We reorganize the Results and Discussion to emphasize the main findings, move selected detailed comparisons to the Supplementary Materials, add effect-summary and subgroup-inference tables, and provide more specific policy implications.
- We conduct a careful language review and standardize grammar, terminology, and figure-caption formatting throughout the manuscript.

We also made many revisions based on other comments by the editor and reviewers, and more detailed responses to each reviewer are enclosed.

Finally, we would like to express our sincere gratitude to the editor and reviewers. We hope that these changes meet your expectations, and we look forward to receiving your decision on the improved version of our manuscript.

# Editor

Thank you for submitting your manuscript, as listed above, to the International Journal of Disaster Risk Reduction. The reviewers have commented on your paper. They indicated that would benefit from minor revision. Hence, I invite you to revise and resubmit your manuscript.

When resubmitting your manuscript, please carefully consider all issues mentioned in the reviewers' comments, outline every change made point by point, and provide suitable rebuttals for any comments not addressed.

I look forward to receiving your revised manuscript in due course.

**Response:**
Thank you for the opportunity to revise our manuscript. We have carefully considered all issues raised by the reviewers and revised the manuscript accordingly. Detailed point-by-point responses are provided below.

# Reviewer 1

## Comment 1

The manuscript addresses a relevant and timely topic, and the analytical framework linking education, climate knowledge, awareness, and adaptive action is generally clear. However, the text would benefit from a careful language revision to correct several minor grammatical and typographical issues. For example, expressions such as "Using Nepal national survey" should be revised to "Using a national survey from Nepal"; "poor-educated groups" should be replaced with "groups with low educational attainment"; and minor errors such as "Nepal is is", "invididual-level", "impact estiamtion", "binary corss-entropy", "validataion", "Specificily", and "eduction" should be corrected throughout the manuscript. The authors should also ensure consistent terminology, particularly by using "adaptive actions" rather than "adaptative actions", and standardize figure captions, for example "Figure 1" instead of "Figure1".

**Response:**
Thank you for this careful and constructive comment. We have corrected all language, terminology, and formatting issues identified by the reviewer and conducted a careful language review of the manuscript.

## Comment 2

In addition, the literature review could be strengthened by citing and briefly discussing the following recent studies, which are relevant to climate adaptation, environmental awareness, and sustainability-related risk reduction: https://doi.org/10.1186/s12302-025-01254-y; https://doi.org/10.3390/environments12050148.

**Response:**
Thank you for this helpful suggestion. We have strengthened the literature discussion in the Introduction by citing and briefly discussing both recommended studies. The study by Lopes et al. (2025) is used to clarify that high climate-risk awareness does not necessarily translate into preparedness and that educational attainment and financial constraints influence adaptive engagement. The review by Ribeiro et al. (2025) situates the Nepal case within the broader geography of sustainability transitions by highlighting the concentration of previous research in the Global North and the value of context-specific evidence from the Global South. Both studies have also been added to the References.

“Recent survey evidence from northern Portugal provides further insight into this relationship, showing that high awareness of climate risks did not necessarily translate into perceived preparedness. Higher educational attainment was associated with greater climate knowledge and stronger engagement in adaptation, whereas financial constraints continued to restrict the translation of awareness into action14.”

(Lines 48-53; Pages 3)

“Moreover, empirical evidence from the Global South is particularly valuable because sustainability-transition research remains disproportionately concentrated in the Global North, even though transition pathways are strongly shaped by local and regional contexts27.”

(Lines 81-84; Pages 5)

14	Lopes, H. S., Silva, P. F., Almeida, M., Ribeiro, I. & Remoaldo, P. Are residents prepared for the effects of climate change? A survey-based study in Tâmega e Sousa (Mainland Portugal). Environmental Sciences Europe 37, 221 (2025). https://doi.org:10.1186/s12302-025-01254-y

27	Ribeiro, I. P., Lopes, H. S., Dinis, M. A. P. & Remoaldo, P. C. Geography of Sustainability Transitions: Mapping Spatial Dynamics and Research Trends Between 1995 and 2024. Environments 12, 148 (2025).

## Overall Comment

Congratulations for your interesting work.

**Response:**
Thank you for your positive and encouraging comment. We sincerely appreciate the time and effort you have devoted to reviewing our manuscript.

# Reviewer 2

## Comment 1

Abstract -

Briefly clarify the study design and whether causal claims are justified from the observational survey data. Also specify what is meant by the "multi-layered analytical framework". Additionally, consider reporting one or two key quantitative findings to better convey the significance of the results.

**Response:**
Thank you for this helpful comment. We have revised the Abstract to clarify the use of observations from the 2016 and 2022 survey waves, define the multi-layered analytical framework, and report key quantitative findings. The revised wording presents the analysis in terms of associations and model-estimated effects, thereby avoiding overly strong causal interpretation. The revised Abstract reads as follows.

"Climate change increasingly threatens livelihoods in developing countries, where adaptive capacity depends heavily on individuals’ ability to understand climatic risks and respond accordingly. Using 11,568 observations from the 2016 and 2022 waves of Nepal’s National Climate Change Impact Survey, this study examines associations between education and climate change knowledge, awareness, and adaptive actions. We construct a multi-layered framework in which XGBoost models are organized into three sequential analytical layers. These layers link education to climate knowledge, climate knowledge to awareness, and both knowledge and awareness to four adaptive actions. Comparisons between factual and counterfactual predictions distinguish model-estimated total, direct and indirect effects. Under the modelled education-improvement scenario, the predicted probability of climate knowledge rises from 46.35% to 51.07%, while the predicted probabilities of the four adaptive actions increase by 0.56-1.15 percentage points. Indirect effects operating through knowledge and awareness are generally larger than the corresponding direct effects. Importantly, the adaptive returns to education are uneven: groups with lower baseline educational attainment, including women, older adults, low-income households, rural residents, and populations in the western Mountain and Hill regions, exhibit larger marginal gains from additional education. Overall, the findings highlight that strengthening education systems, especially for groups with low educational attainment, may offer an effective and equity-enhancing approach to building climate resilience in vulnerable contexts."

(Lines 5-25; Pages 1-2)

## Comment 2

Introduction -

The introduction provides a strong rationale for the study and clearly establishes the importance of education in climate adaptation. It is overly long and could be restructured by reducing background information and avoiding repetition.

**Response:**
Thank you for this helpful comment. We have streamlined the Introduction by consolidating repetitive background information and shortening the Nepal context while retaining the study rationale, key evidence, prioritised research gaps, and corresponding objectives. Examples of the condensed passages are provided below.

"Climate change has emerged as one of the most pressing development challenges worldwide, disproportionately affecting low-income and climate-vulnerable populations 1-3. Rising temperatures, shifting precipitation patterns, and increased frequency of extreme events are already undermining livelihoods, damaging infrastructure, and intensifying risks for communities that lack sufficient adaptive capacity 3-5. In many developing countries, where agricultural dependence is high and social protection remains limited, households’ ability to understand climatic risks and respond effectively becomes a critical determinant of resilience 4,6. Climate adaptation is therefore both a cognitive and behavioral process 7, yet many vulnerable populations lack accurate information or face barriers that prevent awareness from translating into action 8,9."

(Lines 32-42; Pages 3)

"Moreover, empirical evidence from the Global South is particularly valuable because sustainability-transition research remains disproportionately concentrated in the Global North, even though transition pathways are strongly shaped by local and regional contexts 27. Nepal is among the few countries to have implemented nationally representative climate change surveys covering education, climate knowledge, awareness, climate-related experiences, and adaptive behaviors. This unique dataset provides country-specific evidence while offering broader insights for other developing and climate-vulnerable regions."

(Lines 81-89; Pages 5)

## Comment 3

Several gaps stated in the section 52-72 overlap, and the study's novelty would be clearer if they were prioritised and directly linked to the study objectives.

**Response:**
Thank you for this helpful comment. We have revised the Introduction to consolidate the overlapping gaps into three prioritised research gaps and align them directly with three study objectives. The revised structure distinguishes the sequential climate-response pathway, nonlinear model-based estimation, and contextual heterogeneity, thereby clarifying the study's contribution without relying on an absolute novelty claim.

"Despite these insights, three related gaps remain. First, most studies examine climate knowledge, awareness, or adaptive actions separately, leaving the sequential pathway from knowledge through awareness to adaptive actions insufficiently tested with individual-level data that measure all three domains 15,16. Second, the predominance of linear statistical models and qualitative analyses limits the examination of nonlinear relationships and the distinction between education-related associations that operate directly and those that operate through knowledge and awareness 17,18. Third, limited attention has been paid to whether these relationships vary across demographic, socioeconomic, and geographic contexts, even though climate vulnerability is highly uneven within countries 9,19. These limitations leave the mechanisms, magnitude, and contextual heterogeneity of the relationship between education and climate resilience insufficiently understood."

(Lines 53-64; Pages 3-4)

"Against this backdrop, this study has three objectives. First, using nationally representative individual-level data from Nepal, we examine the layered relationship linking education to climate knowledge, awareness of local climate change, and adaptive actions. Second, we apply a multi-layered XGBoost framework with factual-counterfactual prediction comparisons to distinguish model-estimated total effects from their direct and indirect components. Third, we assess how these estimated relationships vary across demographic, socioeconomic, and geographic groups. By integrating sequential climate-response pathways, nonlinear model-based estimation, and contextual heterogeneity within an analytical framework, the study responds directly to the research gaps and offers an integrated account of education’s role in climate responses."

(Lines 90-100; Pages 5)

## Comment 4

The Nepal case study is well described, but the discussion would benefit from more specific evidence or statistics to strengthen the rationale.

**Response:**
Thank you for this helpful comment. The revised Introduction now strengthens the rationale for the Nepal case by adding national survey statistics that show the contrast between widespread climate exposure and limited climate awareness, particularly among rural households. It also explains how this exposure–awareness gap motivates the examination of the progression from education to knowledge, awareness, and adaptive action.

"National survey evidence further illustrates the coexistence of high climate exposure and limited climate awareness in Nepal. Although 87.22% of households reported experiencing climate change over the previous 25 years, only 35.8% were aware of climate change, with awareness falling to 26.3% among rural households. This combination of widespread exposure and limited awareness makes Nepal an especially important setting for examining how education shapes the progression from climate knowledge to awareness and adaptive action."

(Lines 71-77; Pages 4)

## Comment 5

Some claims (e.g., "first systematic empirical assessment" and "first" contributions) should be supported by evidence or softened unless a comprehensive literature review confirms them.

**Response:**
Thank you for this helpful comment. We have revised the Introduction to avoid unsupported absolute novelty claims. The manuscript now describes the contribution as an integrated analytical account without claiming to be the first.

"By integrating sequential climate-response pathways, nonlinear model-based estimation, and contextual heterogeneity within an analytical framework, the study responds directly to the research gaps and offers an integrated account of education’s role in climate responses."

(Lines 98-100; Pages 5)

## Comment 6

Methodology -

The survey data are appropriate for the research objectives, but the authors should provide stronger justification for pooling the 2016 and 2022 survey waves. Specifically, explain how differences in sampling frames (2011 vs. 2021 Census), survey implementation, and temporal changes were accounted for in the analysis.

**Response:**
Thank you for this important comment. We have expanded the Survey Information subsection to explain how the two census-specific sampling frames and temporal differences are addressed when pooling the 2016 and 2022 NCCIS waves. The added paragraph clarifies the common survey implementation and variable-harmonization procedure, the inclusion of survey year in all models, and the repeated cross-sectional interpretation of the pooled estimates.

"Although the sampling frames are updated between survey waves to reflect the most recent population census, each survey is designed to be nationally representative under its corresponding census frame, and both are conducted by the CBS using comparable core survey modules. Because the objective of this study is to estimate average education-related patterns across two nationally representative repeated cross-sectional surveys rather than within-household changes, the two waves are pooled to increase statistical power and sample heterogeneity. To ensure comparability, variable definitions and coding are harmonized, and only measures available in both survey waves are retained. Survey year is included as an explanatory variable in all models to account for systematic differences between survey waves. Accordingly, the pooled estimates are interpreted as average cross-sectional relationships across the two survey periods rather than evidence of temporal change. After excluding observations with missing values, the final dataset for analysis comprises 11,568 observations."

(Lines 119-131; Pages 6-7)

## Comment 7

The description of counterfactual effect estimation could be improved by clarifying the assumptions required to interpret these estimates as causal effects and by discussing potential limitations arising from observational data.

**Response:**
Thank you for this important comment. We have revised the Basic Logic of Effect Estimation subsection to specify how binary-variable prediction sets are constructed, clarify that the comparison remains model-dependent, and define the assumptions and interpretive limits of the model-estimated effects. We have also expanded the Limitations and Future Work section to discuss the limitations arising from the repeated cross-sectional observational data. The specific revisions are presented below.

"For binary variables, we generate two prediction sets by assigning the focal indicator values of one and zero while keeping all other observed variables unchanged. The first prediction assigns the indicator a value of one, as follows:"

(Lines 188-190; Pages 10)

"Similarly, this comparison remains model-dependent and follows the same predictive-performance requirements as the preceding estimation procedure."

(Lines 196-197; Pages 10)

"Counterfactual predictions are generated by systematically modifying one predictor while holding all other observed variables unchanged. The resulting differences are interpreted as model-estimated effects under the learned prediction function rather than experimentally identified causal effects. Their interpretation assumes that the observed covariates adequately capture the major factors associated with both education and climate-related outcomes and that the fitted machine learning model adequately approximates the underlying relationships. Because the NCCIS consists of repeated cross-sectional observational surveys, unobserved confounding cannot be completely ruled out. Accordingly, these estimates provide model-based evidence on the proposed education-related pathways rather than conclusive evidence of causality."

(Lines 202-212; Pages 10-11)

"Despite its contributions, this study has several limitations that offer directions for future research. First, although the nationwide survey provides rich cross-sectional information, the analysis remains observational. The assumptions required for causal identification, including conditional exchangeability, common support, consistency, no interference, and correct temporal ordering, cannot be fully verified with these data. Residual confounding, self-reported measurement error, and the absence of within-household longitudinal observations may therefore affect the model-estimated effects. We consequently interpret the findings as model-based evidence under the specified education-improvement scenarios rather than definitive causal estimates. Future work could employ longitudinal panel data, natural experiments, or randomized information interventions to identify the causal pathways linking education to climate-related cognition and behavior more rigorously."

(Lines 636-647; Pages 35)

## Comment 8

Since the study emphasises "interpretable machine learning", specify which interpretation techniques (e.g., SHAP values, partial dependence plots, feature importance) were used and how they informed the analysis. Also, consider describing how uncertainty from earlier-stage predictions was incorporated into later-stage estimates.

**Response:**
Thank you for this helpful comment. We have clarified in the Methodology that model interpretation uses XGBoost's built-in gain-based feature importance, summarized across 100 fitted models, and explained how these importance values inform comparisons across the three analytical layers. We also clarify that earlier-stage predictions enter subsequent layers as averages of repeated out-of-fold probabilities and explicitly acknowledge that this procedure does not propagate the full distribution of upstream prediction uncertainty. The added methodological descriptions are as follows.

"Model interpretation is based on XGBoost’s built-in gain-based feature importance. For each fitted model, this measure represents the average improvement in the objective function produced by splits involving a given predictor and is normalized across all predictors. We repeat stratified 10-fold cross-validation using 10 random seeds and summarize each predictor’s normalized gain importance by its mean and standard deviation across the resulting 100 fitted models. These importance values are used to compare the relative predictive contributions of education-related variables and the main climate-related variables across the three analytical layers."

(Lines 244-251; Pages 12)

"For each observation, the repeated cross-validation procedure generates one out-of-fold predicted probability from each of the 10 random partitions. We average these 10 probabilities before entering predicted knowledge and awareness as predictors in the subsequent analytical layer. This averaging reduces dependence on any single sample partition, but it does not explicitly propagate the full distribution of uncertainty associated with the upstream predictions. Later-layer estimates are therefore interpreted subject to this limitation."

(Lines 260-266; Pages 13)

## Comment 9

The authors should explicitly discuss the assumptions and limitations of using machine-learning predictions for effect estimation.

**Response:**
Thank you for this important comment. We have clarified the assumptions underlying prediction-based effect estimation in the Basic Logic of Effect Estimation subsection and expanded the fourth point in the Limitations and Future Work section to discuss empirical-support requirements, model extrapolation, cross-layer error propagation, and the distinction between predictive performance and effect-estimate validity.

"Counterfactual predictions are generated by systematically modifying one predictor while holding all other observed variables unchanged. The resulting differences are interpreted as model-estimated effects under the learned prediction function rather than experimentally identified causal effects. Their interpretation assumes that the observed covariates adequately capture the major factors associated with both education and climate-related outcomes and that the fitted machine learning model adequately approximates the underlying relationships. Because the NCCIS consists of repeated cross-sectional observational surveys, unobserved confounding cannot be completely ruled out. Accordingly, these estimates provide model-based evidence on the proposed education-related pathways rather than conclusive evidence of causality."

(Lines 202-212; Pages 10-11)

"Fourth, the model-estimated effects depend on probabilistic predictions generated by the fitted machine-learning models. Their interpretation therefore assumes adequate model fit and sufficient empirical support for the adjusted predictor values; estimates may be less reliable when these adjustments require extrapolation beyond well-represented covariate combinations. Because predictions from earlier layers enter subsequent models, prediction errors may also propagate across the analytical sequence. Cross-validated accuracy evaluates predictive performance but does not by itself validate the resulting effect estimates. Future research could address these limitations by combining probability calibration and overlap diagnostics with explicit propagation of prediction uncertainty across layers and comparison with causal machine-learning approaches."

(Lines 658-668; Pages 36)

## Comment 10

Results -

The results are comprehensive and well organised; however, the section is overly descriptive. Consider focusing on the key findings and moving detailed numerical comparisons to supplementary materials.

**Response:**
Thank you for this helpful comment. We have revised the Results section to focus on the main findings and moved the detailed factual–counterfactual numerical comparisons to a new Detailed Numerical Comparisons subsection in the Supplementary Materials. The main text now summarizes the overall pattern and directs readers to Supplementary Materials Table S2. The revised main-text sentence reads as follows.

"Under the modelled education-improvement scenario, climate knowledge, awareness, and all four adaptive actions increase, with detailed numerical comparisons provided in Supplementary Materials Table S2."

(Lines 350-353; Pages 17)

The corresponding Supplementary Materials text reads as follows.

"Table S2 summarizes the model-estimated total, direct, and indirect effects, with the corresponding numerical comparisons presented below. When education levels are elevated, the mean predicted probability of climate change knowledge rises from 46.35% to 51.07%, an increase of 4.72 percentage points, equivalent to a 10.2% relative gain. Climate change awareness increases from 90.45% to 91.62%, a rise of 1.17 percentage points. For adaptive actions, the mean probabilities increase by 1.15, 0.56, 0.74 and 0.87 percentage points, corresponding to relative improvements of 4.94%, 2.34%, 2.37%, and 2.71%, respectively."

(Lines 112-119; Pages 6)

## Comment 11

The authors conclude that XGBoost is "more suitable" because of its higher predictive accuracy. However, predictive performance alone does not validate the counterfactual effect estimates. This limitation should be acknowledged and discussed.

**Response:**
Thank you for this important comment. We have revised the Results to limit the comparison between XGBoost and logistic regression to their observed cross-validation performance and removed the broader claim that XGBoost is "more suitable" for the analysis. We also explicitly state in the Limitations and Future Work section that predictive accuracy does not by itself validate the model-estimated effects. The revised text and the relevant limitation read as follows.

"Similarly, the fine-tuned XGBoost models achieve average 10-fold cross-validation accuracies of 89.51% for Climate Change Awareness Dummy, and 86.41%, 84.83%, 83.51%, and 86.50% for the four action variables, respectively. These values are higher than the corresponding average validation accuracies of the logistic regression models, which are 42.38%, 56.15%, 63.27%, 66.03%, and 69.52%, respectively. The XGBoost models also show smaller standard deviations in validation accuracy."

(Lines 311-317; Pages 15)

"Fourth, the model-estimated effects depend on probabilistic predictions generated by the fitted machine-learning models. Their interpretation therefore assumes adequate model fit and sufficient empirical support for the adjusted predictor values; estimates may be less reliable when these adjustments require extrapolation beyond well-represented covariate combinations. Because predictions from earlier layers enter subsequent models, prediction errors may also propagate across the analytical sequence. Cross-validated accuracy evaluates predictive performance but does not by itself validate the resulting effect estimates. Future research could address these limitations by combining probability calibration and overlap diagnostics with explicit propagation of prediction uncertainty across layers and comparison with causal machine-learning approaches."

(Lines 658-668; Pages 36)

## Comment 12

The decomposition of total, direct, and indirect effects is interesting but requires a clearer explanation of how these effects were calculated and whether the decomposition is formally equivalent to mediation analysis.

**Response:**
Thank you for this important comment. We have revised the Multi-layered Analysis and Accumulated Effects subsection to define how the total, direct, and indirect effects are calculated from separate factual and counterfactual prediction scenarios. We also clarify that these contrasts are estimated independently under nonlinear XGBoost prediction functions, are not constrained to be additive, and represent a model-based pathway decomposition rather than a formal causal mediation analysis. The added paragraph reads as follows.

"The total effect on climate change knowledge is calculated as the sample-mean change in predicted probability after the education-improvement adjustment, which increases Education Year by one and sets the Literate Education Dummy and Illiterate Dummy to zero. Because knowledge constitutes the first analytical layer, no preceding indirect pathway is involved. For awareness and adaptive actions, we calculate the total, direct, and indirect effects using separate prediction scenarios. The total-effect scenario applies the education adjustment and replaces the predicted probabilities from the preceding layers with their counterfactual values. The direct-effect scenario applies only the education adjustment while retaining the factual upstream probabilities, whereas the indirect-effect scenario retains the factual education variables and replaces only the upstream probabilities with their counterfactual values. Each effect is calculated as the sample mean of the difference between the corresponding counterfactual and factual predicted probabilities. Because these contrasts are estimated separately under nonlinear XGBoost prediction functions, the total effect is not constrained to equal the arithmetic sum of the direct and indirect effects. Therefore, this procedure is interpreted as a model-based pathway decomposition, rather than a formal causal mediation analysis."

(Lines 267-283; Pages 13-14)

## Comment 13

The policy implications drawn from subgroup analyses (e.g., prioritising women, older adults, or low-income groups) should be supported by statistical evidence demonstrating that the observed differences are significant.

**Response:**
Thank you for this important comment. We have added formal between-group tests for the subgroup total effects presented in Figures 4–7 and report the complete results in Supplementary Materials Table S7. The comparisons use standard errors clustered at the survey-year–PSU level, with p-values adjusted across the subgroup comparisons using the Holm procedure. The revised Results specify which subgroup differences are statistically significant, thereby aligning the subgroup-based policy implications with the statistical evidence. The table is provided below.

**Table S7: Subgroup Difference Inference**

[Paste Supplementary Materials Table S7 here]

The relevant additions to the Results read as follows.

"The differences between women and men are statistically significant for climate knowledge, awareness, and all four adaptive actions. These comparisons use standard errors clustered at the survey-year–PSU level, with p-values adjusted across the subgroup comparisons using the Holm procedure, as reported in Supplementary Materials Table S7."

(Lines 391-396; Pages 20)

"The between-group differences are statistically significant only for climate knowledge, awareness, and soil and water conservation."

(Lines 415-417; Pages 22)

"The between-group differences are statistically significant for all outcomes except risk reduction."

(Lines 433-434; Pages 24)

"The differences between rural and urban residents are statistically significant for climate knowledge, awareness, and all four adaptive actions."

(Lines 456-457; Pages 26)

## Comment 14

The manuscript would benefit from a concise summary table reporting the main estimated effects (total, direct, and indirect) across all outcomes and subgroup analyses to improve readability.

**Response:**
Thank you for this helpful comment. To present the results more clearly and in detail, we have added five effect summary tables to the Supplementary Materials. These tables report the model-estimated total, direct, and indirect effects for the overall sample and subgroups. Corresponding references have also been added to the Results section of the main manuscript. The five tables are provided below.

**Table S2: Summary of Model-estimated Total, Direct, and Indirect Effects**

[Paste Supplementary Materials Table S2 here]

**Table S3: Summary of Model-estimated Total, Direct, and Indirect Effects by Gender**

[Paste Supplementary Materials Table S3 here]

**Table S4: Summary of Model-estimated Total, Direct, and Indirect Effects by Age**

[Paste Supplementary Materials Table S4 here]

**Table S5: Summary of Model-estimated Total, Direct, and Indirect Effects by Income**

[Paste Supplementary Materials Table S5 here]

**Table S6: Summary of Model-estimated Total, Direct, and Indirect Effects by Location**

[Paste Supplementary Materials Table S6 here]

## Comment 15

There are numerous grammatical and typographical errors that should be corrected, including "adaptative" (adaptive), "Specificily" (Specifically), "eduction" (education), "clamte" (climate), "accross" (across), "The spatial map show" (shows), and the incomplete sentence 454 "where higher literacy and infrastructural access...".

**Response:**
Thank you for this careful comment. We have corrected all errors identified by the reviewer and conducted a careful language review of the manuscript.

## Comment 16

Discussion -

The manuscript frequently uses strong causal language (e.g., "we prove" and "education effectively improves"), despite relying on cross-sectional observational data. The conclusions should be rephrased to emphasise associations or estimated effects, and the causal interpretation should be presented more cautiously.

**Response:**
Thank you for this important comment. We have reviewed the manuscript and revised the relevant passages to avoid overstating causal interpretation. The revised wording distinguishes model-estimated effects from causal effects, describes knowledge as an intermediate stage in the estimated pathway, and frames the conclusions in terms of relationships and associations. The relevant revised passages read as follows.

"Counterfactual predictions are generated by systematically modifying one predictor while holding all other observed variables unchanged. The resulting differences are interpreted as model-estimated effects under the learned prediction function rather than experimentally identified causal effects. Their interpretation assumes that the observed covariates adequately capture the major factors associated with both education and climate-related outcomes and that the fitted machine learning model adequately approximates the underlying relationships. Because the NCCIS consists of repeated cross-sectional observational surveys, unobserved confounding cannot be completely ruled out. Accordingly, these estimates provide model-based evidence on the proposed education-related pathways rather than conclusive evidence of causality."

(Lines 202-212; Pages 10-11)

"In this sense, knowledge represents an intermediate stage in the model-estimated pathway. Higher education is associated with greater knowledge, which in turn is associated with the recognition and interpretation of climatic change. This layered pattern is consistent with the indirect effect of education on awareness being larger than its direct effect."

(Lines 518-522; Pages 30)

"This study develops and applies a multi-layered machine-learning framework to characterize the relationships among education, climate knowledge, awareness, and adaptive actions in Nepal. The results indicate that these associations operate mainly through interconnected cognitive stages and vary across demographic, socioeconomic, and geographic contexts. By examining these relationships as an interconnected pathway, the study extends climate cognition-behavior research beyond isolated bivariate associations and identifies education as an upstream component of context-dependent adaptive capacity. Overall, the findings suggest that education should be viewed as a core component of national climate-resilience strategies."

(Lines 676-684; Pages 36-37)

## Comment 17

The manuscript describes the proposed framework as a "methodological breakthrough," "new paradigm," and "methodological template" for future studies. These claims appear stronger than the evidence presented.

**Response:**
Thank you for this helpful comment. We have revised the Discussion and Conclusions to calibrate the description of the framework's methodological contribution. Specifically, we removed the unsupported labels "methodological breakthrough," "new paradigm," and "methodological template" and now describe the framework in terms of its specific analytical role and scope. The revised text reads as follows.

"The use of a factual-counterfactual design further enables the decomposition of total, direct, and indirect effects, allowing the identification of hierarchical mechanisms from knowledge to awareness to behavior 28."

(Lines 607-610; Pages 34)

"This integrated framework provides a scalable and transparent tool for examining multilevel processes in climate adaptation research."

(Lines 612-614; Pages 34)

## Comment 18

The discussion repeatedly emphasises the sequential pathway from education, knowledge, awareness, and adaptive behaviour across multiple sections. Similarly, several key findings are restated in the Policy Implications and Conclusions. Consolidating these repeated arguments would improve readability and reduce redundancy. The authors should explicitly state the novel theoretical insight offered by the multilayered analytical framework and explain how it extends prior research on climate cognition and adaptive behaviour.

**Response:**
To improve the clarity and focus of the Discussion, we have removed the detailed restatement of the results from the opening paragraph and retained only a concise overview, with the interpretation of the findings developed in the corresponding subsections. We have also revised the Discussion to more explicitly articulate the study’s novel theoretical contribution. In addition, the Policy Implications and Conclusions have been revised to reduce repetition and avoid restating the main findings. The revised passages read as follows.

"Based on a nationally representative dataset with 11,568 observations and interpretable machine learning techniques, this study explores the associations between education and climate change knowledge, awareness, and adaptive actions. The discussion considers the cognitive pathways underlying these associations, their social and geographic heterogeneity, and their implications for climate adaptation research and policy."

(Lines 480-485; Pages 29)

"Theoretically, our findings extend the Knowledge-Awareness-Behavior/Practice paradigm, which posits that knowledge acquisition precedes attitudinal change and behavioral responses 40-43. Rather than treating education, climate perception, and action as separate bivariate relationships, the multi-layered framework positions education as an upstream enabling condition and links knowledge and awareness as empirically distinguishable cognitive stages through which education is associated with adaptive action 36,44-47.  Consequently, our theoretical contribution lies in conceptualizing education-related adaptation as a context-dependent cognitive pathway, rather than a uniform direct relationship, and in showing that the strength of its component links varies across social and geographic groups."

(Lines 543-552; Pages 31)

**Implications for Climate Adaptation Policy**

"The model-estimated pathways support combining long-term educational investment with climate-specific communication in adaptation planning, particularly in developing and climate-vulnerable contexts such as Nepal. First, investments in basic literacy and lower-secondary schooling can be complemented by environmental science content, climate-related modules in informal education programs, and experiential learning approaches 32. Second, community-based climate extension services, localized early-warning systems, and targeted campaigns can connect educational gains to accessible, context-specific climate information 25,26,37. Third, programs that expand educational opportunities for women, low-income households, and rural populations may be particularly relevant 25,26,51. Moreover, in the western Mountain and Hill regions, school facilities, adult education, and climate communication infrastructure could receive particular attention because these areas combine high climate risk with low literacy. National education and environment agencies could coordinate implementation in partnership with provincial and local governments, schools, and community-based organizations. Taken together, the policy measures should incorporate education and climate communication into national climate-resilience planning."

(Lines 617-633; Pages 34-35)

**Conclusions**

"This study develops and applies a multi-layered machine-learning framework to characterize the relationships among education, climate knowledge, awareness, and adaptive actions in Nepal. The results indicate that these associations operate mainly through interconnected cognitive stages and vary across demographic, socioeconomic, and geographic contexts. By examining these relationships as an interconnected pathway, the study extends climate cognition-behavior research beyond isolated bivariate associations and identifies education as an upstream component of context-dependent adaptive capacity. Overall, the findings suggest that education should be viewed as a core component of national climate-resilience strategies."

(Lines 676-684; Pages 36-37)

## Comment 19

The policy recommendations are relevant but remain relatively broad. The authors could enhance this section by proposing more specific, actionable recommendations, such as identifying priority educational interventions, implementation mechanisms, or institutional stakeholders.

**Response:**
Thank you for this helpful suggestion. We have revised the Implications for Climate Adaptation Policy section to provide more specific and actionable recommendations. The revised paragraph identifies priority educational interventions, target populations and regions, implementation mechanisms, and institutional stakeholders that could coordinate implementation. The revised paragraph reads as follows.

"The model-estimated pathways support combining long-term educational investment with climate-specific communication in adaptation planning, particularly in developing and climate-vulnerable contexts such as Nepal. First, investments in basic literacy and lower-secondary schooling can be complemented by environmental science content, climate-related modules in informal education programs, and experiential learning approaches 32. Second, community-based climate extension services, localized early-warning systems, and targeted campaigns can connect educational gains to accessible, context-specific climate information 25,26,37. Third, programs that expand educational opportunities for women, low-income households, and rural populations may be particularly relevant 25,26,51. Moreover, in the western Mountain and Hill regions, school facilities, adult education, and climate communication infrastructure could receive particular attention because these areas combine high climate risk with low literacy. National education and environment agencies could coordinate implementation in partnership with provincial and local governments, schools, and community-based organizations. Taken together, the policy measures should incorporate education and climate communication into national climate-resilience planning."

(Lines 617-633; Pages 34-35)
