#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import os

# 单独放入.py文件中，导入不了，所以直接放到此处，待修复
firstnames = """一 乙 乃 了 力 丁 刀 刁 二 又 人 入 七 十 几 口 干 工 弓 久 己 土 大 丈 女 己 巾 勺 丸 也 于 弋 巳 兀 三 下 上 乞 士 夕 千 子 寸 小 山 川 巳 才 凡 公 孔 亢 勾 中 之 丹 井 介 今 内 及 太 天 屯 斗 斤 牛 丑 支 允 元 勿 午 友 尤 尹 引 文 月 日 牙 王 云 匀 牛 四 丑 仁 什 切 升 收 壬 少 心 手 日 氏 水 尤 仍 双 尺 仇 止 才 不 互 分 匹 化 卡 卞 肥 反 夫 巴 幻 户 方 木 比 毛 仆 丰 火 片 古 切 可 瓜 甘 刊 五 丘 加 去 句 叫 外 巧 巨 玉 甲 令 加 占 主 巨 冬 他 代 只 仗 另 句 召 尼 正 田 旦 奴 凸 立 叮 仝 伏 台 奶 凹 五 外 央 右 未 永 以 戊 玉 瓦 由 幼 仕 巧 丘 仙 兄 司 且 史 左 世 出 市 玄 仔 冉 穴 示 生 申 充 主 仞 仟 册 加 去 只 叫 求 正 甲 申 石 匝 甩 丙 平 母 弘 末 包 本 弗 北 必 丕 半 布 皿 目 乏 禾 皮 疋 矛 乎 付 兄 卉 戊 民 冰 玄 白 卯 伉 光 匡 共 各 考 交 件 价 企 伍 伎 仰 吉 圭 曲 机 艮 六 仲 吉 州 朱 兆 决 匠 地 旨 朵 吏 列 年 劣 同 打 汀 至 臼 灯 竹 老 舟 伎 吊 吏 圳 的 宅 机 老 肉 虫 伊 仰 伍 印 因 宇 安 屹 有 羊 而 耳 衣 亦 吃 夷 奸 聿 丞 企 休 任 先 全 再 冲 刑 向 在 夙 如 宅 守 字 存 寺 式 戌 收 早 旭 旬 曲 次 此 求 系 肉 臣 自 舌 血 行 圳 西 休 交 件 企 匠 吉 尖 而 至 色 伏 后 名 回 好 妃 帆 灰 牟 百 份米 伐 亥 卉 冰 刑 合 向 旭 朴 系 行 汜 复 克 告 改 攻 更 杆 谷 况 伽 估 君 吴 吸 吾 圻 均 坎 研 完 局 岐 我 扣 杞 江 究 见 角 言 住 占 低 佃 况 里 冷 伶 利 助 努 君 吝 昌 壮 妓 妞 局 弄 廷 弟 彤 志 托 杖 杜 呆 李 江 男 究 良 见 角 具 皂 里 舟 佟 你 体 足 甸 町 豆 吞 玎 位 佐 佘 冶 吾 吟 吴 吻 完 尾 巫 役 忘 我 修 言 邑 酉 吟 吴 研 呆 角 七 伸 佐 作 些 伽 些 初 吹 呈 坐 孝 宋 岐 希 岑 床 序 巡 形 忍 成 杏 材 杉 束 村 杞 步 汝 汐 池 私 秀 赤 足 身 车 辰 系 占 伺 住 余 助 劭 劬 邵 吸 坐 壮 妆 局 床 志 汕 江 灶 见 即 却 克 早 何 布 伯 伴 佛 兵 判 别 含 坊 坂 吵 宏 旱 每 甫 牡 况 免 孚 孝 尾 巫 希 庇 形 忙 杏 呆 步 汛 贝 儿 供 侃 刻 卦 固 坤 姑 官 冈 庚 快 抗 昆 果 空 亟 其 具 券 卷 奇 委 季 宜 居 届 岢 岸 杰 佳 京 侄 佳 来 例 制 到 兔 两 典 卷 周 呢 坦 奈 妮 宙 定 居 屉 帖 底 店 征 忝 忠 念 技 投 政 枝 东 林 汰 决 玖 知 的 直 纠 金 两 乳 侏 佰 侗 佻 佬 具 冽 卓 拈 妲 妯 宕 岱 岭 帖 帙 底 抒 林 杼 沓 炉 竺 长 依 侑 味 夜 委 宜 宛 岳 岸 岩 往 亚 武 於 易 昂 旺 沅 沃 汪 物 艾 卧 佯 儿 咏 抑 昀 炎 杳 事 享 侍 使 侈 然 刹 刺 协 卒 洽 沁 取 受 步 垂 奇 始 炊 姓 妻 妾 尚 屈 弦 所 承 昌 升 昔 松 欣 沙 沈 社 舍 炊 采 长 青 幸 亟 徇 佳 舍 儿 争 其 刷 券 制 效 卷 姐 姒 姗 季 炙 宗 届 岫 征 承 昔 析 枕 状 八 并 佩 函 和 命 坡 坪 奉 孟 帛 水 府 佛 彼 忽 或 戽 房 扮 枇 扶 放 昏 朋 服 明 杭 杯 枚 板 沛 沐 汾 版 牧 虎 门 阜 杷 盲 非 冠 奎 皈 客 故 柑 柯 况 看 科 肝 革 屋 癸 砍 禹 轨 页 九 亭 亮 柱 俊 侣 冒 段 劲 南 姬 姜 姣 宦 帝 度 痔 建 峙 待 律 怠 急 招 拒 拓 拙 拉 昭 架 柱 柳 注 治 炭 界 皆 突 纪 纣 耐 肚 致 计 订 军 酊 俐 胃 百 厘 咨 姝 姿 柁 沱 炭 妆 纣 重 珏 盅 眈 俄 俞 勇 威 娃 姻 姚 姨 屋 幽 彦 奕 哀 哇 玟 怡 押 映 昱 韦 油 泳 沿 姚 畏 烟 盈 禹 约 耶 衍 要 页 音 昱 易 柚 胤 易 信 侠 系 俗 促 俏 前 则 奏 型 姹 妊 姝 姿 室 宣 巷 咱 哉 思 性 施 昨 是 春 星 查 柴 栅 柔 染 泉 帅 甚 相 省 砂 祈 秋 穿 肖 重 首 酉 食 香 侵 俟 峙 旭 注 沐 炷 祉 贞 昌 泓 侯 保 便 冒 勉 匍 奔 品 佩 杯 封 哈 皇 拔 抱 怕 柏 柄 泌 法 泡 炳 玫 盆 眉 红 美 虹 秒 表 负 面 风 飞 眄 胃 勃 厚 咸 叛 孩 奂 屏 枰 某 河 泛 赴 库 恭 拱 格 桂 根 耕 耿 股 肯 贡 高 个 刚 哥 宫 径 挂 皋 径 徒 倜 恬 拯 指 拿 料 旅 晋 朕 桌 桔 桃 桐 洞 流 洛 酒 烈 特 玲 珍 真 矩 祝 秩 租 站 级 纸 纳 纽 者 肩 芝 记 讨 酌 酒 针 钉 只 挑 借 倒 值 俱 倪 倘 伦 兼 唐 哲 娘 旃 娟 娜 展 峻 准 凌 洲 套 爹 特 留 俩 倜 庭 恫 耻 烙 料 栗 株 津 玳 畜 砧 恩 按 案 鸟 洋 秧 翁 纹 耘 育 芽 芸 蚊 袁 烟 倚 原 员 埃 宴 峨 倚 娱 容 峪 晏 移 益 差 师 席 座 徐 恰 息 恕 肩 持 拳 拾 时 书 曹 校 朔 桑 栽 殊 气 洽 珊 祠 神 祖 秦 秤 索 素 纱 纾 纯 虔 讫 训 财 起 轩 芩 闪 迅 倩 幸 修 仓 城 夏 孙 宰 容 射 峡 厝 叟 奚 畜 春 乘 借 准 淞 宵 指 拭 牲 洵 洳 狩 兹 珊 炸 租 站 宸 挈 旁 晃 桓 活 洪 畔 亩 眠 破 炮 秘 粉 纺 肺 肥 航 般 芳 芙 花 配 马 侯 倍 俯 俸 们 圃 埋 娩 峰 肪 涵 畔 埔 害 恢 恍 恒 柏 派 洹 玻 泌 珉 祜 呗 国 寇 昆 康 苦 袍 规 贯 够 勘 崞 岗 梗 珙 偕 假 健 停 侦 剪 动 翎 念 基 坚 堂 堆 婧 寄 专 张 得 教 救 朗 条 梁 梯 械 梨 浙 浪 珠 略 皎 眷 窕 竟 第 终 累 舵 苓 架 诀 近 钓 顶 鸟 将 那 庶 振 挺 捉 捐 甜 祭 趾 囵 堆 凌 崃 带 帐 徕 悌 画 梁 梃 桶 町 娄 伟 偶 务 唯 问 婉 寅 尉 帷 庸 悟 悠 悦 敖 晚 梧 浴 眼 研 移 胃 苑 英 迎 野 鱼 欲 浣 翌 圉 乾 做 区 卿 参 售 启 商 唱 娶 妇 宿 崇 崎 崔 常 强 从 悄 叙 旋 晨 晟 族 消 爽 犀 祥 绅 细 紫 组 绍 婧 羞 习 邢 舷 船 茄 若 处 术 袖 设 讼 责 赦 雀 雪 顷 彩 常 孰 侦 匙 圊 执 将 专 就 峥 崧 巢 庶 彩 悉 施 曹 浙 笙 钏 阡 凰 毫 培 婚 婆 妇 密 彬 彪 患 斌 曼 海 浩 烽 班 瓶 毕 盒 符 邦 胡 背 胞 胖 舶 范 茅 苗 袍 被 觅 访 货 返 贩 闭 麦 麻 邦 壶 票 冕 副 埠 屏 涵 捕 敏 皓 梅 第 珩 艴 苹 敢 款 淦 筐 给 贵 辜 开 凯 昆 诒 询 几 蛟 植 堵 堤 奠 岚 帧 掌 掘 捷 掏 掎推 探 接 敦 景 智 晶 替 朝 椒 棠 栈 殖 淘 添 淡 净 焦 街 诊 理 荔 眨 贴 屠 贷 轸 迢 迪 迦 量 钧 钮 间 集 杰 劳 单 婷 喋 传 塘 塔 暖 楠 殿 渡 汤 帏 幄 惟 掩 椅 涯 液 渊 焰 为 异 砚 围茵 越 阮 轶 雁 雅 寓 云 雯 媛 喻 贻 婺 焱 琬 琰 畲 劳 博 堡 报 富 寒 嵋 帽 幅 帮 弼 复 彭徨 偏 整 理 惠 扉 排 斑 酣 普 棉 棒 棚 涵 混 淼 淮 淝 牌 画 番 发 皓 脉 茗 评 贺 费 买 贸 迫 邯 闵 防 阪 黄 傅 傍 媒 媚 黑 瓿 匮 块 干 感 揆 手 楷 港 琨 莞 夸 鼓 该 贾 传 仅 涂 塔 塘 廊 谦 提 敬 斟 极 楠 殿汤 渡 绢 经 茎 莒 获 莅 庄 莉 蜀 里 装 解 詹 鼎 贾 路 迹 退 铃 钜 陀 电 雷 靖 顿 暖 桢 路 嫁 农 贮 贷 贴 轸 迪 钠 湍 琳 当 略 铃 鼓 励 庸 园 圆 奥 爱 意 扬 援 握 榆 业 杨 椰涌 渝 渭 游 炜 爷 烟 兽 犹 煜 碗 筠 义 肄 莞 莠 虞 蛾 裕 诣 郁 钰 雍 阿 预 饮 衙 莹 蓊 晕 渥 琬 琰 畹 筵 裔 淡 催 传 勤 势 嗣 塞 嵩 厦 新 喧 楸 楚 岁湘 测 凑 煦 琴 琪 琦 睡 祺 稔 稠 筮 粲 绣 群 圣 莎 裙 诩 诗 试 诠 详 资 载 送 铅 阻 雌 颂 驰 熙 暄 琼 塞 嵩 想 桢 椿 岁 渚 煮 琛 庄 裟 输 轼 幕 汇 惶 挥 描 换 楣 枫 湖 浑 渺 涣 煤烦 琶 琥 盟 睦 碑 禀 聘 腑 荷 莫 号 蜂 补 话 酩 附 颁 饭 晕 募 焕 廓 愧 沟 管 纲 诰 闺 魁 构 歌 恺 斡 荣构 嘏 通 连 这 甄 兢 喜 团 图 奖 嫡 对 僚 侥屡 嶂 崭 彰 廖 熊 溜 监 祯 种 端 箕 筝 精 绿 紧 绫 纶 置 璋 畅 榔 糍 滇 尔 莱 赵 铬 领 瑙 奁 闻 嫣 愿 温 源 溢 尔 瑜 瑛 瑗 玮 与舞 苑 诱 语 郢 银 摇 榕 荣 温 荥 溶 菸 菀 鞅 瑛 僖 逑 速 逍 肾 寿 塾 尘 嫩 实 像 侨 岖 慈滋 沧 溶 溪 熊 狮 瑞 瑟 硕 算 粹 绸 综 绰 绮 翠 菁 菜 菖 裳 认 誓 诵 说 诚 轻 菘 造 速 衔 铨 限 需 韶 饲 饰 旗 畅 荣 榕 齐 熏 僦 尝 墅 奖 实 寨 慎 准 溯 搴 逢 梦 仆 幕 滑 瑚 珲 碧 福 绵 翡 腑 萍华 菩 蜜 裴 豪 宾 辅 郝 铭 阀 陌 颇 饮 凤 鸣 榜 槐 滏 宽 广 慷 惯 概 瑰 葛 葵 课 逵 郭 稿 靠溉 锆 俭 著 价 厉 剧 剑 刘 妖 履 帜 弹 徵 德虑 摘 敌 整 暂 椿 闾 乐 楼 樟 滴 渐 涨 浆 练 缔 蒂 骀 落 董 葶 蝶 调 谆 谈 诋 诤 谅 论 质 驼 践 轮 逮 进 醇 铝 阵 震 霆 驾 驻 稽 稻 稷 节 剪 几 鲁 黎 侬 涤 墩 幢 嶙 锻 褚 亿 仪 影 慰 忧 乐 样 欧 毅 演 渔 熬 熠熨 瑶 缘 纬 腰 万 莹 叶 苇 谊 逸 邮 阅 院 鞍 颐 养 欲 颍 粗 缓 卫 葳 骑 妩 鉴 署 啸 增 婵 审 层 厂 厨 厮 庆 摧 数 枢漆 熟 热 线 肠 兴 萱 冲 褚 谁 请 贤 赏 赐 趣 娴 醉 锐 销 爽 霄 驷 确 磁 穷 箭 箱 竖 辍 帜 漩 渐 箴 节 绪 翦 葸 诤 谆 质 醇 罚 划 哗 坟 墨 币 庙 废 慧 慕 慢 暮 樊标 模 流 浒 汉 满 漫 漂 玛 缓 编 腹 铺 葆 葡 复 卖 赋 辉 辈 部 锋 陛 盘 码 篇 范 麾 劈 幡 慧 摩 沪 漠 磐 褒 弼 荭 窥 糕 膏 盖 钢 龟 购 器 垦 横 橄 篙 馆尽 坛 导 惮 战 撰 整 历 瞳 昙 暨 机 橘 洁 潭 灯 瑾 璋 庐 积 筑 蒸 诸 谛 诺 练 猪 赖 蹄 辑 道 达 都 录 锦 锭 陆 陶 陵 霓 霖 静 颊 头 雕 疆 腿 臻 赚 骆 莅 俦 橙 润 澈 笃 缙 萤 萤 卫 谓 谒 谙 谕 豫 逾 游 运 阴 余 壅赢 蓉 蓊 勋 儒 器 学 宪 熹 憧 晓 桥 樵 橙 橡 树润 潮 甑 莳 璇 聪 融 亲 谌 谐 输 遂 醒 举 莲 蔗 蒋 讲 递 辗 镀 锻 钟 键 隆 队 骏 黛 点 泽 沣 潞 澄 优 婴 屿 狱 赢 应 忆 拥 澳 营 蔚 荫 舆锾 闱 阳 偿 择 擅 操 泽 澡 燧 禧 穗 簇 纵 总 聪声 膝 襄 谦 逮 邹 乡 隋 虽 霞 霜 鲜 戏 鸿 壕 嫔 弥 帮 桧 篷 缝 繁 褒 锚 韩 蔓徵 擘 扶 柜 圹 归 缋 蒉 磬 纩 戴 拟 抬 挤 爵 涛 礼 简 粮 职 旧 蕉 谨转 遮 题 镇 储 藜 芷 迟 鲤 翼 芸 讴 医 隘 额 瑷 莸 镒 隗 彝 潍 储 丛 曙 湿 织 萧 蕊 蝉 瑞 适 双 绣 锁垒 戴 断 柠 涛 泞 璐 礼 粮 藜 槟 滨 获 壁 环 蕃 丰 庞 璧 馥 扩 关 铿 庐 疆 祷 荐 勒 襟 谭 证 轿 辽 邻 郑 邓类 鲸 丽 麓 镜 觉 际 橹 栎 泺 辚 链 韵 稳 薏 薇 膺 臆 蚁 袄 遗 雾 愿 艳 蓣蕹 韫 玺 薛 薪 绳 蟹 识 赞 遵 迁 选 庞 渖 荐谯 镟 锵 镞 铲 际 颡 鹑 暹 攀 簿 绘 鹏 庞 瀑 宝 祢 薜 谱 镆 镘 矿 阚 岿 藉 蓝 拢 沥 泷 竞 篮 罗 舰 觉 警 钟 露 腾 党 枥 槠 滤 濑 炉 窦 笞 筹 镦 荩 严 瀛 耀 译 议 邀 懿 赢 萨 藏 薰 壤 悬 曦 琼 筹 脐 馨 释 献 坏 孀 籍 藉 谵 锈 钟 宝 怀 瀚 缤 还 迈 飘 膑 朦 濒 铧 顾 钚 俪 栏 铁 鸡 镯 藤 览 镭 铎 铛 膑 丽 斓 樱 艺 藕 誉 跃 迩 莺 险 续 随 属 攘 誉 茑 鸡 藩 轰 辩 癖 霸 鹤 钚 灌 垄 叠 笼 听 芦 览 读 铸 籁 苈 链 懿 蔼 隐 璎 蕴 鳙 欢 边 鳗 镔 沣 镬 矿 恋 兰 体 滩 铄 鳞 驿 验 缨 织 显 钻 变 蘩 罐 赣 雳 灵 陇 酿 鹰 霭 坝 嬖 观 戆 厅 篱 钥 瑷 镶 黉 颢 逻 驴 湾 灒 銮 骥 湾 钻 骧 鹦 艳 鹳 郁 吁"""
lastnames = """赵 钱 孙 李 周 吴 郑 王 冯 陈 楮 卫 蒋 沈 韩 杨 朱 秦 尤 许 何 吕 施 张 孔 曹 严 华 金 魏 陶 姜 戚 谢 邹 喻 柏 水 窦 章 云 苏 潘 葛 奚 范 彭 郎 鲁 韦 昌 马 苗 凤 花 方 俞 任 袁 柳 酆 鲍 史 唐 费 廉 岑 薛 雷 贺 倪 汤 滕 殷 罗 毕 郝 邬 安 常 乐 于 时 傅 皮 卞 齐 康 伍 余 元 卜 顾 孟 平 黄 和 穆 萧 尹 姚 邵 湛 汪 祁 毛 禹 狄 米 贝 明 臧 计 伏 成 戴 谈 宋 茅 庞 熊 纪 舒 屈 项 祝 董 梁 杜 阮 蓝 闽 席 季 麻 强 贾 路 娄 危 江 童 颜 郭 梅 盛 林 刁 锺 徐 丘 骆 高 夏 蔡 田 樊 胡 凌 霍 虞 万 支 柯 昝 管 卢 莫 经 房 裘 缪 干 解 应 宗 丁 宣 贲 邓 郁 单 杭 洪 包 诸 左 石 崔 吉 钮 龚 程 嵇 邢 滑 裴 陆 荣 翁 荀 羊 於 惠 甄 麹 家 封 芮 羿 储 靳 汲 邴 糜 松 井 段 富 巫 乌 焦 巴 弓 牧 隗 山 谷 车 侯 宓 蓬 全 郗 班 仰 秋 仲 伊 宫 宁 仇 栾 暴 甘 斜 厉 戎 祖 武 符 刘 景 詹 束 龙 叶 幸 司 韶 郜 黎 蓟 薄 印 宿 白 怀 蒲 邰 从 鄂 索 咸 籍 赖 卓 蔺 屠 蒙 池 乔 阴 郁 胥 能 苍 双 闻 莘 党 翟 谭 贡 劳 逄 姬 申 扶 堵 冉 宰 郦 雍 郤 璩 桑 桂 濮 牛 寿 通 边 扈 燕 冀 郏 浦 尚 农 温 别 庄 晏 柴 瞿 阎 充 慕 连 茹 习 宦 艾 鱼 容 向 古 易 慎 戈 廖 庾 终 暨 居 衡 步 都 耿 满 弘 匡 国 文 寇 广 禄 阙 东 欧 殳 沃 利 蔚 越 夔 隆 师 巩 厍 聂 晁 勾 敖 融 冷 訾 辛 阚 那 简 饶 空 曾 毋 沙 乜 养 鞠 须 丰 巢 关 蒯 相 查 后 荆 红 游 竺 权 逑 盖 益 桓 公 万俟 司马 上官 欧阳 夏侯 诸葛 闻人 东方 赫连 皇甫 尉迟 公羊 澹台 公冶 宗政 濮阳 淳于 单于 太叔 申屠 公孙 仲孙 轩辕 令狐 锺离 宇文 长孙 慕容 鲜于 闾丘 司徒 司空 丌官 司寇 仉 督 子车 颛孙 端木 巫马 公西 漆雕 乐正 壤驷 公良 拓拔 夹谷 宰父 谷梁 晋 楚 阎 法 汝 鄢 涂 钦 段干 百里 东郭 南门 呼延 归 海 羊舌 微生 岳 帅 缑 亢 况 后 有 琴 梁丘 左丘 东门 西门 商 牟 佘 佴 伯 赏 南宫 墨 哈 谯 笪 年 爱 阳 佟 第五 言 福"""

class ChineseName(object):
    """中文名取名"""
    def __init__(self, firstname_file=None, lastname_file=None):
        """初始化
        Args:
            firstname_file: 文件路径 - String
            lastname_file：文件路径 - String
            以上两个路径参数有默认值，也可由用户自定义，文件内容以空格分隔即可
        Returns:
            _firstnames：存储名字，便于多次调用 - List
            _lastnames：存储姓氏，便于多次调用 - List
        """
        if firstname_file != None:
            self._firstnames=self._getChars(firstname_file)
        else:
            self._firstnames = firstnames.split(" ")

        if lastname_file != None:
            self._lastnames=self._getChars(lastname_file)
        else:
            self._lastnames = lastnames.split(" ")

    def _getChars(self, filename):
        """获取中文字符列表
        Args:
            filename: 文件路径 - String (空格分隔文件)
        Returns:
            List: 字符列表
        Raise:
            file not find
        """
        if os.path.exists(filename):
            with open(filename, "r") as f:
                chars = f.read().split(" ")
                return chars
        else:
            raise IOError("file not find!")
  
    def getLastName(self):
        """获取姓氏
        Args:
            None
        Returns:
            String: 姓氏
        """
        lastname = random.choice(self._lastnames)
        return lastname

    def getFirstName(self, char_count=1):
        """获取名字
        Args:
            char_count: 名字长度，默认1 - Integer
        Returns:
            String: 名字
        """
        firstname = []
        for i in range(char_count):
            firstname.append(random.choice(self._firstnames))

        firstname = "".join(firstname)
        return firstname

    def getName(self, char_count=1, lastname=""):
        """获取一个中文名字
        Args:
            char_count: 名字长度，默认1 - Integer
            lastname: 姓氏，默认随机 - String
        Returns:
            String: 名字
        """
        name = []
        if lastname == "":
            name.append(self.getLastName())
        else:
            name.append(lastname)

        name.append(self.getFirstName(char_count))
        name = "".join(name)
        return name

    def getNames(self, count, char_count=1, lastname=""):
        """获取一个中文名字列表
        Args:
            count: 名字数量 - Integer
            char_count: 名字长度，默认1 - Integer
            lastname： 姓氏，默认随机 - String
        Returns:
            List: 名字列表
        """
        names = []
        for i in range(count):
            names.append(self.getName(char_count,lastname))
        return names

    def getNameGenerator(self, count, char_count=1, lastname=""):
        """获取一个中文名字生成器，2018年1月22日
        Args:
            count: 名字数量 - Integer
            char_count: 名字长度，默认1 - Integer
            lastname： 姓氏，默认随机 - String
        Returns:
            Yield：姓名生成器
        """
        for i in range(count):
            yield self.getName(char_count, lastname)
        

def main():
    chinesename = ChineseName()     # 初始化，可以指定姓氏文件
    name = chinesename.getName(lastname="白")  # 获取一个姓名
    print(name)
    names=chinesename.getNames(100,char_count=2,lastname="彭")   # 获取一个姓名列表
    print(names)

    # 获取一个姓名生成器
    name_generator = chinesename.getNameGenerator(10)
    for name in name_generator:
        print(name)


if __name__ == '__main__':
    main()
