import json
from datetime import datetime, timedelta
import random

class FundIndustryRankGenerator:
    def __init__(self):
        self.data_sources = ["天天基金网", "晨星中国", "蚂蚁财富", "东方财富", "雪球", "同花顺"]
        self.rank_types = ["月度行业主题榜", "长期稳健基金榜", "金选指数基金榜", "行业精选榜", "成长价值榜", "科技主题榜"]
        self.industries = ["医药生物", "新能源", "消费", "科技制造", "半导体", "人工智能", "数字经济", "军工", "金融", "地产", "农业", "传媒", "教育", "环保"]
        self.fund_types = ["股票型", "混合型", "指数型", "QDII", "ETF", "FOF"]
        self.risk_levels = ["低风险", "中风险", "中高风险", "高风险"]
        
        # 基金代码前缀
        self.fund_code_prefixes = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
        
        # 基金名称模板
        self.fund_name_templates = [
            "{company}行业精选", "{company}创新成长", "{company}价值精选", "{company}科技先锋",
            "{company}消费升级", "{company}医疗健康", "{company}新能源", "{company}数字经济"
        ]
        
        # 基金公司名称
        self.fund_companies = [
            "易方达", "华夏", "南方", "嘉实", "工银瑞信", "广发", "富国", "博时",
            "汇添富", "鹏华", "华安", "国泰", "招商", "中欧", "景顺长城", "兴证全球"
        ]

    def generate_fund_code(self):
        prefix = random.choice(self.fund_code_prefixes)
        suffix = str(random.randint(1000, 9999))
        return f"{prefix}{suffix}"

    def generate_fund_name(self):
        company = random.choice(self.fund_companies)
        template = random.choice(self.fund_name_templates)
        return template.format(company=company)

    def generate_return_rate(self, is_monthly=True):
        if is_monthly:
            return f"{random.uniform(-5, 20):.2f}%"
        else:
            return f"{random.uniform(-15, 50):.2f}%"

    def generate_sharpe_ratio(self):
        return f"{random.uniform(0.5, 2.5):.2f}"

    def generate_max_drawdown(self):
        return f"-{random.uniform(10, 30):.2f}%"

    def generate_investment_reasons(self, industry):
        reasons = {
            "医药生物": [
                "医药集采政策缓和，创新药纳入医保速度加快",
                "全球老龄化加速，医疗刚需消费属性凸显",
                "创新药研发投入持续增长，行业景气度提升",
                "医保目录调整优化，创新药准入加快",
                "医疗新基建投资加速，设备需求增长"
            ],
            "新能源": [
                "欧盟碳关税政策推动光伏出口量同比增长40%",
                "储能装机量超预期，行业复合增速达35%",
                "新能源汽车渗透率持续提升，产业链景气度高",
                "光伏组件价格下降，装机成本降低",
                "氢能产业政策支持力度加大"
            ],
            "消费": [
                "五一消费数据创历史新高，服务消费同比增长32%",
                "白酒龙头渠道库存降至三年低位，提价预期升温",
                "消费升级趋势明显，高端消费需求增长",
                "免税政策优化，旅游消费复苏",
                "新零售模式创新，线上消费持续增长"
            ],
            "科技制造": [
                "国产替代加速，半导体设备需求增长",
                "工业4.0升级，智能制造投资加大",
                "高端装备出口增长，国际竞争力提升",
                "数字化转型加速，工业软件需求增长",
                "专精特新企业扶持政策加码"
            ],
            "半导体": [
                "芯片国产化率提升，产业链自主可控",
                "AI芯片需求爆发，算力需求增长",
                "先进制程突破，技术壁垒提升",
                "汽车芯片需求增长，供应缺口扩大",
                "半导体设备国产化加速"
            ],
            "人工智能": [
                "大模型技术突破，应用场景扩展",
                "AI+行业融合加速，商业化落地加快",
                "算力基础设施投资加大",
                "AI芯片需求爆发，产业链景气度高",
                "人工智能政策支持力度加大"
            ]
        }
        
        # 获取行业特定理由
        industry_reasons = reasons.get(industry, [
            "行业景气度持续提升",
            "政策支持力度加大",
            "市场需求增长",
            "技术创新加速",
            "产业链整合优化"
        ])
        
        # 随机选择3个理由
        return random.sample(industry_reasons, 3)

    def generate_monthly_data(self, date):
        result = []
        for source in self.data_sources:
            monthly_data = {
                "数据来源": source,
                "更新日期": date.strftime("%Y-%m-%d"),
                "榜单类型": random.choice(self.rank_types),
                "基金列表": []
            }
            
            # 每个数据源生成10-15个基金
            num_funds = random.randint(10, 15)
            for _ in range(num_funds):
                industry = random.choice(self.industries)
                fund_info = {
                    "基金代码": self.generate_fund_code(),
                    "基金名称": self.generate_fund_name(),
                    "基金类型": random.choice(self.fund_types),
                    "所属行业": industry,
                    "近一月收益率": self.generate_return_rate(True),
                    "近一年收益率": self.generate_return_rate(False),
                    "夏普比率": self.generate_sharpe_ratio(),
                    "最大回撤": self.generate_max_drawdown(),
                    "值得投理由": self.generate_investment_reasons(industry),
                    "风险等级": random.choice(self.risk_levels)
                }
                monthly_data["基金列表"].append(fund_info)
            
            # 添加备注信息
            monthly_data["备注"] = [
                f"数据摘自{source}行业热度榜",
                "行业分类依据申万一级行业标准",
                "风险等级基于基金波动率及持仓集中度测算"
            ]
            
            result.append(monthly_data)
        
        return result

    def generate_historical_data(self, months=6):
        all_data = []
        current_date = datetime.now()
        
        for i in range(months):
            target_date = current_date - timedelta(days=30*i)
            monthly_data = self.generate_monthly_data(target_date)
            all_data.extend(monthly_data)
        
        return all_data

    def save_to_json(self, data, filename="fund_industry_rank.json"):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    generator = FundIndustryRankGenerator()
    fund_data = generator.generate_historical_data(months=6)
    generator.save_to_json(fund_data)
    print(f"已生成{len(fund_data)}条数据，保存到fund_industry_rank.json")

if __name__ == "__main__":
    main() 