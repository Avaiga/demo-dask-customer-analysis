from taipy import Config

from algos.algo import (
    preprocess_and_score,
    featurization_and_segmentation,
    segment_analysis,
    high_value_cust_summary_statistics,
)

# -------------------- Data Nodes --------------------

path_to_data_cfg = Config.configure_data_node(id="path_to_data", default_data="data/customers_data.csv")

scored_df_cfg = Config.configure_data_node(id="scored_df")

payment_threshold_cfg = Config.configure_data_node(id="payment_threshold", default_data=1000)

score_threshold_cfg = Config.configure_data_node(id="score_threshold", default_data=1.5)

segmented_customer_df_cfg = Config.configure_data_node(id="segmented_customer_df")

metric_cfg = Config.configure_data_node(id="metric", default_data="mean")

segment_result_cfg = Config.configure_data_node(id="segment_result")

summary_statistic_type_cfg = Config.configure_data_node(id="summary_statistic_type", default_data="median")

high_value_summary_df_cfg = Config.configure_data_node(id="high_value_summary_df")

# -------------------- Tasks --------------------

preprocess_and_score_task_cfg = Config.configure_task(
    id="preprocess_and_score",
    function=preprocess_and_score,
    skippable=True,
    input=[path_to_data_cfg],
    output=[scored_df_cfg],
)

featurization_and_segmentation_task_cfg = Config.configure_task(
    id="featurization_and_segmentation",
    function=featurization_and_segmentation,
    skippable=True,
    input=[scored_df_cfg, payment_threshold_cfg, score_threshold_cfg],
    output=[segmented_customer_df_cfg],
)

segment_analysis_task_cfg = Config.configure_task(
    id="segment_analysis",
    function=segment_analysis,
    skippable=True,
    input=[segmented_customer_df_cfg, metric_cfg],
    output=[segment_result_cfg],
)

high_value_cust_summary_statistics_task_cfg = Config.configure_task(
    id="high_value_cust_summary_statistics",
    function=high_value_cust_summary_statistics,
    skippable=True,
    input=[segment_result_cfg, segmented_customer_df_cfg, summary_statistic_type_cfg],
    output=[high_value_summary_df_cfg],
)

scenario_cfg = Config.configure_scenario(
    id="scenario_1",
    task_configs=[
        preprocess_and_score_task_cfg,
        featurization_and_segmentation_task_cfg,
        segment_analysis_task_cfg,
        high_value_cust_summary_statistics_task_cfg,
    ],
)
