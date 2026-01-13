# ZIP 損壞檔案報告

**報告日期**: 2026-01-07

**總損壞檔案數**: 113 個

---

## 摘要

索引過程中發現 113 個 Excel 檔案的 ZIP 結構損壞，無法正常開啟。

**問題描述**:
- ZIP 檔案缺少結尾標記（End-of-central-directory signature）
- 可能原因：Sharepoint 同步未完成、網路傳輸中斷、檔案下載不完整

**影響**:
- 這些檔案無法被索引
- Python、Excel、LibreOffice 均無法開啟
- 需要從 Sharepoint 重新下載

---

## 按目錄分類

### Deneb - Documents/01_Project_Management

**數量**: 56 個檔案

1. **(Discussion)Copy of Sirius_QG3_BCM_20220929.xlsx**
   - 大小: 57.95 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.06_Miscellaneous/BCM/(Discussion)Copy of Sirius_QG3_BCM_20220929.xlsx`

2. **20230704 C-sample User plan .xlsx**
   - 大小: 9.78 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3225_UX_plan_update/20230704 C-sample User plan .xlsx`

3. **BCM_Good practice example.xlsx**
   - 大小: 54.92 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.06_Miscellaneous/BCM/BCM_Good practice example.xlsx`

4. **BOSCH_Deneb Schedule Acceleration Plan B_0517.xlsx**
   - 大小: 51.54 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Schedule/Primax/20230517/BOSCH_Deneb Schedule Acceleration Plan B_0517.xlsx`

5. **BT_VS_ETW_Lessons Learned_database_Deneb_draft.xlsx**
   - 大小: 9.54 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG5_Include TAA/6070_Lessons_Learned/BT_VS_ETW_Lessons Learned_database_Deneb_draft.xlsx`

6. **BT_VS_ETW_Lessons Learned_database_Deneb_draft.xlsx**
   - 大小: 9.54 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.11_Lessons_learned/BT_VS_ETW_Lessons Learned_database_Deneb_draft.xlsx`

7. **Bosch Deneb DFMEA_0929_review.xlsx**
   - 大小: 105.36 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2130_DFMEA/Old/Bosch Deneb DFMEA_0929_review.xlsx`

8. **Bosch Deneb DFMEA_1017.xlsx**
   - 大小: 106.96 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2130_DFMEA/Old/Bosch Deneb DFMEA_1017.xlsx`

9. **Bosch Deneb DFMEA_20230512.xlsx**
   - 大小: 103.70 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3230_DFMEA/Old/Bosch Deneb DFMEA_20230512.xlsx`

10. **Bosch Deneb DFMEA_20230512.xlsx**
   - 大小: 103.70 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG3/4105_PPA/Bosch Deneb DFMEA_20230512.xlsx`

11. **Bosch Deneb DFMEA_20230516 - Bosch.xlsx**
   - 大小: 363.66 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3230_DFMEA/Old/Bosch Deneb DFMEA_20230516 - Bosch.xlsx`

12. **Bosch Deneb DFMEA_20230516.xlsx**
   - 大小: 103.56 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3230_DFMEA/Old/Bosch Deneb DFMEA_20230516.xlsx`

13. **Bosch Deneb DFMEA_20230705.xlsx**
   - 大小: 390.08 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3230_DFMEA/Old/Bosch Deneb DFMEA_20230705.xlsx`

14. **Bosch Deneb DFMEA_20230717.xlsx**
   - 大小: 370.05 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3230_DFMEA/Bosch Deneb DFMEA_20230717.xlsx`

15. **Bosch Deneb QG1 DFMEA_1018.xlsx**
   - 大小: 97.38 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2130_DFMEA/Bosch Deneb QG1 DFMEA_1018.xlsx`

16. **Budge plan_20220831.xlsx**
   - 大小: 234.21 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Budget Plan/Budge plan_20220831.xlsx`

17. **Budget_Grand Master Test ODM Plan Deneb.xlsx**
   - 大小: 2.18 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Budget Plan/Budget_Grand Master Test ODM Plan Deneb.xlsx`

18. **Copy of DENEB Material Authorization_LT less than 90D_0418_to BOSCH.xlsx**
   - 大小: 57.46 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.06_Miscellaneous/Copy of DENEB Material Authorization_LT less than 90D_0418_to BOSCH.xlsx`

19. **Copy of Deneb Project Acceleration Plan_0104 for BOSCH_Bosch feedback0116.xlsx**
   - 大小: 81.07 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Schedule/Pull in Jun/Previous/Copy of Deneb Project Acceleration Plan_0104 for BOSCH_Bosch feedback0116.xlsx`

20. **Copy of Deneb_MTP sample plan-20221101_Bosch1115.xlsx**
   - 大小: 44.89 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.08_Sample/Primax/Copy of Deneb_MTP sample plan-20221101_Bosch1115.xlsx`

21. **Copy of Primax_Deneb_MTP Cost_ (version 1).xlsx**
   - 大小: 919.19 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Budget Plan/Primax quote/Copy of Primax_Deneb_MTP Cost_ (version 1).xlsx`

22. **Copy of Primax_Deneb_MTP Cost_.xlsx**
   - 大小: 920.25 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Budget Plan/Primax quote/Copy of Primax_Deneb_MTP Cost_.xlsx`

23. **Deneb First PO.xlsx**
   - 大小: 21.68 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG4/5010_First_order_to_supplier/Deneb First PO.xlsx`

24. **Deneb MTP HW Schedule_A-run-20220802.xlsx**
   - 大小: 42.20 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Schedule/MTP/Deneb MTP HW Schedule_A-run-20220802.xlsx`

25. **Deneb N33.6 BTFR-00024-002_FRM_N_EN_2023-07-05_update.xlsx**
   - 大小: 37.72 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3270_N33.6_QG2/Deneb N33.6 BTFR-00024-002_FRM_N_EN_2023-07-05_update.xlsx`

26. **Deneb Project Acceleration Plan_0207.xlsx**
   - 大小: 92.57 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Schedule/Pull in Jun/Previous/Deneb Project Acceleration Plan_0207.xlsx`

27. **Deneb_DTLP_20221107_2156.xlsx**
   - 大小: 167.61 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2156_Technical_communication_Material/Deneb_DTLP_20221107_2156.xlsx`

28. **Deneb_Lessons_learned.xlsx**
   - 大小: 24.06 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG5_Include TAA/6070_Lessons_Learned/Deneb_Lessons_learned.xlsx`

29. **Deneb_Price update list.xlsx**
   - 大小: 910.66 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Cost topic/Primax priceup/Deneb_Price update list.xlsx`

30. **Deneb_QG1_BCM_20220825.xlsx**
   - 大小: 53.91 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2350_BCM/Deneb_QG1_BCM_20220825.xlsx`

31. **Deneb_QG1_BCM_20220825.xlsx**
   - 大小: 54.59 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.06_Miscellaneous/BCM/Deneb_QG1_BCM_20220825.xlsx`

32. **Deneb_Risk assessment.xlsx**
   - 大小: 3.22 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.06_Miscellaneous/Risk_assessment_archive/Deneb_Risk assessment.xlsx`

33. **Deneb_Sample plan.xlsx**
   - 大小: 67.37 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.08_Sample/Deneb_Sample plan.xlsx`

34. **Deneb_Sample plan_20220524.xlsx**
   - 大小: 67.27 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.08_Sample/Deneb_Sample plan_20220524.xlsx`

35. **Deneb_forecast_SMARC_demand_simulation_20230713.xlsx**
   - 大小: 57.43 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.06_Miscellaneous/Deneb_forecast_SMARC_demand_simulation_20230713.xlsx`

36. **Deneb_sample plan to Primax_20220607.xlsx**
   - 大小: 24.58 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.08_Sample/Deneb_sample plan to Primax_20220607.xlsx`

37. **Deneb_sample plan to Primax_20220610.xlsx**
   - 大小: 24.54 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.08_Sample/Deneb_sample plan to Primax_20220610.xlsx`

38. **Deneb_sample plan to Primax_20220811.xlsx**
   - 大小: 24.75 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.08_Sample/Deneb_sample plan to Primax_20220811.xlsx`

39. **ETW_PAS1_3_Project_Costs (1).xlsx**
   - 大小: 256.91 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Expense/RBTW_EHV_COR_monthly_report/ETW_PAS1_3_Project_Costs (1).xlsx`

40. **ETW_PAS1_3_Project_Costs_Deneb_20231102.xlsx**
   - 大小: 257.17 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Expense/RBTW_EHV_COR_monthly_report/ETW_PAS1_3_Project_Costs_Deneb_20231102.xlsx`

41. **Example_for_Primax_BCM_Good practice.xlsx**
   - 大小: 53.65 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.06_Miscellaneous/BCM/Example_for_Primax_BCM_Good practice.xlsx`

42. **Grand Master Test ODM Plan Deneb V1.1.xlsx**
   - 大小: 2.18 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG0/1058_A_sample/Grand Master Test ODM Plan Deneb V1.1.xlsx`

43. **Grand Master Test ODM Plan Deneb V1.1.xlsx**
   - 大小: 2.17 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2153_MTP/Grand Master Test ODM Plan Deneb V1.1.xlsx`

44. **Grand Master Test ODM Plan Deneb V1.2.xlsx**
   - 大小: 2.17 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2153_MTP/Grand Master Test ODM Plan Deneb V1.2.xlsx`

45. **Grand Master Test ODM Plan Deneb V1.2.xlsx**
   - 大小: 2.17 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3332_TG_acceptance_test_spec_MTP/Grand Master Test ODM Plan Deneb V1.2.xlsx`

46. **Master Tracker_Deneb_as_of_20230427.xlsx**
   - 大小: 738.60 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Expense/RBTW_EHV_COR_monthly_report/Master Tracker_Deneb_as_of_20230427.xlsx`

47. **PIT_RASIC_Deneb_20221114_to PCS.xlsx**
   - 大小: 42.08 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2230_Product_introduction_checklist/PIT_RASIC_Deneb_20221114_to PCS.xlsx`

48. **PIT_RASIC_Deneb_20221115.xlsx**
   - 大小: 39.03 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2160_MarCom_material/PIT_RASIC_Deneb_20221115.xlsx`

49. **PIT_RASIC_Deneb_20230706.xlsx**
   - 大小: 60.11 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3320_Product_Introduction_checklist_update/PIT_RASIC_Deneb_20230706.xlsx`

50. **Primax MTP plan Dec-21.xlsx**
   - 大小: 945.38 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2153_MTP/Primax MTP plan Dec-21.xlsx`

51. **Primax MTP plan Dec-26.xlsx**
   - 大小: 945.49 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2153_MTP/Primax MTP plan Dec-26.xlsx`

52. **Project expense for QG0 jusi.xlsx**
   - 大小: 294.48 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Project expense for QG0 jusi.xlsx`

53. **Project-spendings.xlsx_0713_Deneb.xlsx**
   - 大小: 18.11 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.04_Time Cost Planning/Budget Plan/Project-spendings.xlsx_0713_Deneb.xlsx`

54. **SOCOS_Copy of CGP-03825-008_BBL_N_EN_2015-10-22.xlsx**
   - 大小: 859.08 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG1/2350_BCM/SOCOS_Copy of CGP-03825-008_BBL_N_EN_2015-10-22.xlsx`

55. **Sirius_QG3_BCM_20220922.xlsx**
   - 大小: 57.15 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.06_Miscellaneous/BCM/Sirius_QG3_BCM_20220922.xlsx`

56. **data for infographic (1).xlsx**
   - 大小: 51.99 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/01_Project_Management/1.07_Milestones/QG2/3322_MarCom_material_English_released/data for infographic (1).xlsx`

### Deneb - Documents/03_Quality_Management

**數量**: 4 個檔案

1. **Bosch Deneb DFMEA_1006.xlsx**
   - 大小: 101.53 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/03_Quality_Management/3.03_FMEA/Bosch Deneb DFMEA_1006.xlsx`

2. **Bosch Deneb DFMEA_1011.xlsx**
   - 大小: 101.55 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/03_Quality_Management/3.03_FMEA/Bosch Deneb DFMEA_1011.xlsx`

3. **Bosch Deneb DFMEA_1017.xlsx**
   - 大小: 106.96 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/03_Quality_Management/3.03_FMEA/Bosch Deneb DFMEA_1017.xlsx`

4. **Bosch Deneb DFMEA_1018.xlsx**
   - 大小: 101.25 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/03_Quality_Management/3.03_FMEA/Bosch Deneb DFMEA_1018.xlsx`

### Deneb - Documents/04_Engineering

**數量**: 25 個檔案

1. **Albert_Deneb_A2_Sample_Template+Driver_Verification_List_20220815_v2.xlsx**
   - 大小: 4.10 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.04_Software/A_Run/Driver_Verification_List/ODM FW/Albert_Deneb_A2_Sample_Template+Driver_Verification_List_20220815_v2.xlsx`

2. **Albert_Deneb_A2_Sample_Template+Driver_Verification_List_20220815_v2.xlsx**
   - 大小: 4.10 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.04_Software/A_Run/Driver_Verification_List/Bosch FW/Albert_Deneb_A2_Sample_Template+Driver_Verification_List_20220815_v2.xlsx`

3. **BTFR-09032-000_FRM_N_EN Deneb QG0.xlsx**
   - 大小: 142.28 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.01_SRS/Focus Matrix/BTFR-09032-000_FRM_N_EN Deneb QG0.xlsx`

4. **Deneb 2M sensor board A-sample layout review 20220622-pri.xlsx**
   - 大小: 628.26 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/Sensor/2M/Deneb 2M sensor board A-sample layout review 20220622-pri.xlsx`

5. **Deneb 5M sensor board A-sample layout review 20220622-pri.xlsx**
   - 大小: 157.82 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/Sensor/5M/Deneb 5M sensor board A-sample layout review 20220622-pri.xlsx`

6. **Deneb 8M sensor board A-sample layout review 20220621.xlsx**
   - 大小: 1.03 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/Sensor/8M/Deneb 8M sensor board A-sample layout review 20220621.xlsx`

7. **Deneb A EE report review 20220915.xlsx**
   - 大小: 590.76 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/Test reports/Deneb A EE report review 20220915.xlsx`

8. **Deneb A sample ME MTP test report1214.xlsx**
   - 大小: 43.30 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.02_Mechanical/A run/ME design review/A sample MTP/Deneb A sample ME MTP test report1214.xlsx`

9. **Deneb A-sample schematic review 2022060117.xlsx**
   - 大小: 428.46 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/Deneb A-sample schematic review 2022060117.xlsx`

10. **Deneb A-sample schematic review 20220602.xlsx**
   - 大小: 468.55 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/Deneb A-sample schematic review 20220602.xlsx`

11. **Deneb D run Layout change list_0510.xlsx**
   - 大小: 875.04 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/D-sample/Deneb D run Layout change list_0510.xlsx`

12. **Deneb IO board A-sample layout review 20220624.xlsx**
   - 大小: 161.22 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/IO/Deneb IO board A-sample layout review 20220624.xlsx`

13. **Deneb SD board A-sample layout review 20220624-pri.xlsx**
   - 大小: 84.90 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/SD/Deneb SD board A-sample layout review 20220624-pri.xlsx`

14. **Deneb carrier board A-sample layout review 20220627.xlsx**
   - 大小: 3.23 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/Carrier/Deneb carrier board A-sample layout review 20220627.xlsx`

15. **Deneb power board A-sample layout review 20220616.xlsx**
   - 大小: 134.06 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/Power/Deneb power board A-sample layout review 20220616.xlsx`

16. **Deneb_Derating_20221004_review.xlsx**
   - 大小: 53.30 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/Deneb_Derating_20221004_review.xlsx`

17. **Deneb_Derating_20230508.xlsx**
   - 大小: 41.24 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/Deneb_Derating_20230508.xlsx`

18. **Deneb_IK10-loading-force-calculation.xlsx**
   - 大小: 2.60 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.02_Mechanical/A run/ME design review/Deneb_IK10-loading-force-calculation.xlsx`

19. **Deneb_IK10-loading-force-calculation.xlsx**
   - 大小: 2.93 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.02_Mechanical/A run/ME design review/A sample MTP/Deneb_IK10-loading-force-calculation.xlsx`

20. **M5 Screw Head to Bottom Cover TA Report_BOSCH DENEB_20220907.xlsx**
   - 大小: 148.63 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.02_Mechanical/A run/ME design review/A sample DRM/A sample improvement/TA for M5 screw head under Bottom cvoer's hole/M5 Screw Head to Bottom Cover TA Report_BOSCH DENEB_20220907.xlsx`

21. **ODM_EVA_reference_C_Sample_ME-20210608.xlsx**
   - 大小: 258.06 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.02_Mechanical/A run/ME design review/A sample MTP/ODM_EVA_reference_C_Sample_ME-20210608.xlsx`

22. **Polaris Deneb and Sirius HW comparison.xlsx**
   - 大小: 52.32 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/A-sample/Polaris Deneb and Sirius HW comparison.xlsx`

23. **Polaris Deneb and Sirius HW comparison.xlsx**
   - 大小: 52.50 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.03_Electrical/Polaris Deneb and Sirius HW comparison.xlsx`

24. **Primax_Deneb_A2_Sample_Template+Driver_Verification_List_20220729.xlsx**
   - 大小: 55.15 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.04_Software/A_Run/Driver_Verification_List/ODM FW/Primax_Deneb_A2_Sample_Template+Driver_Verification_List_20220729.xlsx`

25. **Template+Driver_Verification_List.xlsx**
   - 大小: 41.00 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/04_Engineering/4.04_Software/RFQ/FW_Related_Document/Template+Driver_Verification_List.xlsx`

### Deneb - Documents/05_Industrialization

**數量**: 1 個檔案

1. **Copy of Deneb-Ramp up_Global Total_correct cal.xlsx**
   - 大小: 100.67 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/05_Industrialization/5.06_IPS/IPS qty/Copy of Deneb-Ramp up_Global Total_correct cal.xlsx`

### Deneb - Documents/08_Testing_and_Approbation

**數量**: 6 個檔案

1. **DENEB C run EE MTP_0221.xlsx**
   - 大小: 52.40 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/08_Testing_and_Approbation/8.03_Sample_Testing/C sample run/EE pre-C test/DENEB C run EE MTP_0221.xlsx`

2. **Deneb A EE SI report 0830.xlsx**
   - 大小: 62.58 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/08_Testing_and_Approbation/8.03_Sample_Testing/A sample run/EE/Old/Deneb A EE SI report 0830.xlsx`

3. **Deneb A EE SI report 0921.xlsx**
   - 大小: 68.42 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/08_Testing_and_Approbation/8.03_Sample_Testing/A sample run/EE/Deneb A EE SI report 0921.xlsx`

4. **Grand Master Test ODM Plan Deneb V1.1.xlsx**
   - 大小: 2.18 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/08_Testing_and_Approbation/Grand Master Test ODM Plan Deneb V1.1.xlsx`

5. **MTP FW control list.xlsx**
   - 大小: 233.85 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/08_Testing_and_Approbation/MTP FW control list.xlsx`

6. **Project_IR_Illumination_Uniformity_Data_V1.0.xlsx**
   - 大小: 213.30 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/08_Testing_and_Approbation/8.03_Sample_Testing/A sample run/Image/Bosch test condition/Project_IR_Illumination_Uniformity_Data_V1.0.xlsx`

### Deneb - Documents/09_RFQ

**數量**: 1 個檔案

1. **Grand Master Test ODM Plan Deneb.xlsx**
   - 大小: 2.18 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/09_RFQ/01_ODM_RFQ/RFQ_attachment/Grand Master Test ODM Plan Deneb.xlsx`

### Deneb - Documents/10_Meeting

**數量**: 16 個檔案

1. **Deneb Bosch-Primax Weekly Project Meeting_20220713.xlsx**
   - 大小: 143.64 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/RC meeting/20220712/Deneb Bosch-Primax Weekly Project Meeting_20220713.xlsx`

2. **Deneb Bosch-Primax Weekly Project Meeting_20220927.xlsx**
   - 大小: 144.99 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20220928/Deneb Bosch-Primax Weekly Project Meeting_20220927.xlsx`

3. **Deneb Bosch-Primax Weekly Project Meeting_20221025.xlsx**
   - 大小: 145.56 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20221025/Deneb Bosch-Primax Weekly Project Meeting_20221025.xlsx`

4. **Deneb Bosch-Primax Weekly Project Meeting_20221101.xlsx**
   - 大小: 145.12 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20221101/Deneb Bosch-Primax Weekly Project Meeting_20221101.xlsx`

5. **Deneb Bosch-Primax Weekly Project Meeting_20230322.xlsx**
   - 大小: 151.39 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/RC meeting/20230321/Deneb Bosch-Primax Weekly Project Meeting_20230322.xlsx`

6. **Deneb Bosch-Primax Weekly Project Meeting_20230407.xlsx**
   - 大小: 152.60 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20230407/Deneb Bosch-Primax Weekly Project Meeting_20230407.xlsx`

7. **Deneb Bosch-Primax Weekly Project Meeting_20230705.xlsx**
   - 大小: 159.37 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20230705/Deneb Bosch-Primax Weekly Project Meeting_20230705.xlsx`

8. **Deneb_Bosch-Primax_OPL_MTP_Risk_20220609-TW-Z00440.xlsx**
   - 大小: 142.91 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20220608/Deneb_Bosch-Primax_OPL_MTP_Risk_20220609-TW-Z00440.xlsx`

9. **Deneb_OPL_MTP_Risk_20220608-TW-Z00440.xlsx**
   - 大小: 139.77 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20220608/Deneb_OPL_MTP_Risk_20220608-TW-Z00440.xlsx`

10. **Deneb_Risk assessment.xlsx**
   - 大小: 2.49 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/2023-Jun_ETW_risk_assessment_review/Deneb_Risk assessment.xlsx`

11. **OPL_Deneb Bosch-Primax Weekly Project Meeting_20220629.xlsx**
   - 大小: 142.33 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20220629/OPL_Deneb Bosch-Primax Weekly Project Meeting_20220629.xlsx`

12. **OPL_Deneb Bosch-Primax Weekly Project Meeting_20220707.xlsx**
   - 大小: 142.66 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20220707/OPL_Deneb Bosch-Primax Weekly Project Meeting_20220707.xlsx`

13. **OPL_Deneb Bosch-Primax Weekly Project Meeting_20220713.xlsx**
   - 大小: 143.64 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20220713/OPL_Deneb Bosch-Primax Weekly Project Meeting_20220713.xlsx`

14. **OPL_Deneb Bosch-Primax Weekly Project Meeting_20220720.xlsx**
   - 大小: 144.02 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20220720/OPL_Deneb Bosch-Primax Weekly Project Meeting_20220720.xlsx`

15. **OPL_Deneb Bosch-Primax Weekly Project Meeting_20220803.xlsx**
   - 大小: 145.49 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20220803/OPL_Deneb Bosch-Primax Weekly Project Meeting_20220803.xlsx`

16. **OPL_Deneb Bosch-Primax Weekly Project Meeting_20220907.xlsx**
   - 大小: 143.70 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/10_Meeting/Supplier/20220908/OPL_Deneb Bosch-Primax Weekly Project Meeting_20220907.xlsx`

### Deneb - Documents/12_Team_list

**數量**: 1 個檔案

1. **Deneb Bullet Team Roster_PMX updated.xlsx**
   - 大小: 2.26 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/12_Team_list/Deneb Bullet Team Roster_PMX updated.xlsx`

### Deneb - Documents/Deneb Change log & Price risk list.xlsx

**數量**: 1 個檔案

1. **Deneb Change log & Price risk list.xlsx**
   - 大小: 175.50 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/Deneb Change log & Price risk list.xlsx`

### Deneb - Documents/Deneb_ME_IPS_MAT_tracking_2023-Jun_Bosch_team.xlsx

**數量**: 1 個檔案

1. **Deneb_ME_IPS_MAT_tracking_2023-Jun_Bosch_team.xlsx**
   - 大小: 3.25 MB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/Deneb_ME_IPS_MAT_tracking_2023-Jun_Bosch_team.xlsx`

### Deneb - Documents/Master Tracker_Deneb.xlsx

**數量**: 1 個檔案

1. **Master Tracker_Deneb.xlsx**
   - 大小: 758.48 KB
   - 路徑: `/var/www/html/excel_Bosch/Sharepoint/Deneb - Documents/Master Tracker_Deneb.xlsx`

---

## 建議處理方式

1. **短期**: 使用已成功索引的 186 個檔案（56% 覆蓋率）
2. **中期**: 從 Sharepoint 重新同步這 113 個檔案
3. **長期**: 檢查 Sharepoint 同步設定，避免未來再次發生

