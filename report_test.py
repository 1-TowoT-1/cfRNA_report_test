from jinja2 import Environment, Template, FileSystemLoader
import csv
import os

# 定义函数，处理表格数据
def read_tsv_file_and_convert(file_path,row_max):
    data = []
    row_num = 0
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            if row_num < row_max:
                row_num+=1
                data.append(row)
            else:
                break
    return data

QC_result=read_tsv_file_and_convert(r'C:\Users\91361\Desktop\report\src\files\1.QC\QC_result.txt',40)
summary_result=read_tsv_file_and_convert(r'C:\Users\91361\Desktop\report\src\files\summary.txt',40)
#DEG_file文件可能是多个，以逗号隔开，目前测试只做一个，因为通常的DEG就是做的癌症跟健康样本
TMM_file_name=os.path.basename('src/files/2.EXP/TMM_result.txt')
DEG_file_name=os.path.basename('src/files/3.DEG/Treatment_vs_Control_DEseq2.xls')
DEG_summary=read_tsv_file_and_convert(r'C:\Users\91361\Desktop\report\src\files\3.DEG\summary.txt',2)
DEG_anno_summary=read_tsv_file_and_convert(r'C:\Users\91361\Desktop\report\src\files\3.DEG\deg_anno_summary.txt',2)
PPI_relation=read_tsv_file_and_convert(r'C:\Users\91361\Desktop\report\src\files\3.DEG\PPI_relation.xls',40)

# 准备变量
report_data ={
    'title' : '肝癌cfRNA检测报告',
    'logo' : 'src/img/logo.png',
    'pipeline' : 'src/img/pipeline.png',
    # 1.质控
    'QC' : 'src/img/质控.png',
    'base_R1' : 'src/img/1.QC/base_R1.png',
    'base_R2' : 'src/img/1.QC/base_R2.png',
    'GC_R1' : 'src/img/1.QC/GC_R1.png',
    'GC_R2' : 'src/img/1.QC/GC_R2.png',
    'QC_result' : QC_result,
    'summary' : summary_result,
    
    # 2.比对
    'element' : 'src/img/2.MAP/element.png',
    'insertsize' : 'src/img/2.MAP/insertSize.png',
    'saturation' : 'src/img/2.MAP/Saturation.png',

    # 3.定量
    'TMM_file' : 'src/files/2.EXP/TMM_result.txt',
    'TMM_file_name' : TMM_file_name,
    'Gene_class' : 'src/img/3.EXP/Gene_class.png',
    'Box_exp' : 'src/img/3.EXP/box.png',
    'Density_exp' : 'src/img/3.EXP/density.png',
    'Correlation' : 'src/img/3.EXP/correlation.png',
    'PCA' : 'src/img/3.EXP/PCA.png',

    # 4.差异
    'DEG_file' : 'src/files/3.DEG/Treatment_vs_Control_DEseq2.xls',
    'DEG_file_name' : DEG_file_name,
    'volcano' : 'src/img/4.DEG/Treatment_vs_Control_volcano.png',
    'DEG_summary' : DEG_summary,
    'DEG_heatmap' : 'src/img/4.DEG/DEG_heatmap.png',
    'DEG_anno_summary' : DEG_anno_summary,
    'GO_Anno' : 'src/img/4.DEG/GO_classification.png',
    'GO_Enrich_bubble' : 'src/img/4.DEG/GO_enrichment.png',
    'KEGG_Anno' : 'src/img/4.DEG/KEGG_classification.png',
    'KEGG_Enrich_bubble' : 'src/img/4.DEG/KEGG_enrichment.png',
    'KEGG_map' : 'src/img/4.DEG/kegg_map.png',
    'PPI_dat' : PPI_relation,
    'PPI_plot' : 'src/img/4.DEG/PPI.png',
    'GSEA_plot' : 'src/img/4.DEG/gseaplot.png',

    #5.lncRNA-mRNA互作：
    'lncRNA_mRNA' : 'src/img/5.lncRNA/lncRNA-mRNA.png',

    #6. circRNA分析：
    'circRNA_identify' : 'src/img/6.circRNA/circRNA-identify.png',
    'circRNA_exon_num' : 'src/img/6.circRNA/circRNA_exon_num.png',
    'circRNA_Anno' : 'src/img/6.circRNA/circRNA_Anno.png'
}


# 创建HTML模板：
env = Environment(loader=FileSystemLoader(r'C:\Users\91361\Desktop\report'))
template = env.get_template('report.html')
html_report = template.render(report_data)

# 保存HTML报告到文件
with open('C:/Users/91361/Desktop/report/result.html', 'w') as f:
    f.write(html_report)

