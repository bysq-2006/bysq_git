function cj(){
    let doc = document.getElementById("content");
    doc.innerHTML = `
    <h1 class='cj'>学校学生成就展示</h1>

    <div class="student" style="transition: transform 0.3s ease; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
        <img style="height: 300px; width: 600px; display: block; margin: 0 auto 10px auto;" src="./png/CBD675A5934E41448406DB2CEDF_C26AAF6E_79533.png" alt="学生2照片">
        <div class="info" style="padding: 20px; background-color: #f9f9f9; border-radius: 10px; opacity: 0; animation: fadeIn 1s forwards;">
            <h2>天津国赛银奖</h2>
            <p>2024年10月29日 -11月2日在天津举行的世界职业院校技能大赛数字艺术设计赛项中，四川邮电职业技术学院的学生团队凭借稳定的表现荣获国赛银奖。
                <br><br>
                四川邮电职业技术学院的学生团队在激烈的竞争中脱颖而出，在比赛中学生团队不仅展现了数字艺术设计的创新性和技术性，还体现了团队的协作精神和职业素养。学院对于此次比赛给予高度重视，早在备赛前已联合多部门制定了全面而细致的备赛计划，从专业技能的训练到心理素质的培养，从比赛策略的研究到后勤保障的完善，每一个环节都精心策划和反复推敲。
                <br><br>
                此次获奖不仅是对四川邮电职业技术学院学生专业技能和创新能力的肯定，也是对学院教育教学改革和人才培养模式创新的一次重要检验。学院将继续弘扬工匠精神，坚持以赛促教、以赛促学、以赛促改，深化职业教育改革，为培养更多具有创新能力的高素质技能人才贡献力量。</p>
            <p>日期：2024年11月</p>
        </div>
    </div>

    <div class="student" style="transition: transform 0.3s ease; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
        <div class="info" style="padding: 20px; background-color: #f9f9f9; border-radius: 10px; opacity: 0; animation: fadeIn 1s forwards;">
            <h2 style="color: #333; font-family: 'Arial', sans-serif;">全国职业院校技能大赛</h2>
            <p style="color: #555; font-family: 'Arial', sans-serif;">2020年，学校学生获得2020年全国职业院校技能大赛改革试点赛四川省选拔赛“移动应用开发大赛”三等奖1项、“网络系统管理大赛”三等奖1项；职业院校英语演讲比赛获得国家级二等奖1项；第八届全国高校数字艺术设计大赛国赛三等奖1项，省二等奖3项，三等奖4项；第十一届蓝桥杯全国软件和信息技术专业人才大赛国赛三等奖1项，省级二等奖2项；第十五届四川省大学生计算机作品赛省级一等奖3项，二等奖2项；第十届“新华三杯”全国大学生数字技术大赛省级一等奖3项，二等奖3项；三等奖3项；2020全国英语演讲大赛（高职组）二等奖。</p>
            
            <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                <thead>
                    <tr style="background-color: #4CAF50; color: white;">
                        <th style="padding: 10px; border: 1px solid #ccc;">类别</th>
                        <th style="padding: 10px; border: 1px solid #ccc;">名称</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #f2f2f2;">国家骨干院校重点专业</td>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #ffffff;">通信技术<br>移动通信技术<br>网络系统管理<br>市场营销<br>光纤通信</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #ffffff;">国家现代学徒制试点优秀专业</td>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #f2f2f2;">光通信技术专业<br>数字媒体应用技术</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #f2f2f2;">中央财政专项支持的提升专业服务能力建设项目</td>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #ffffff;">通信工程设计与管理<br>通信网络与设备<br>物流管理</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #ffffff;">中央财政专项支持建设实训基地</td>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #f2f2f2;">通信类专业实训基地<br>通信工程设计实训基地<br>数字媒体创意与设计实训基地</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #f2f2f2;">国家级生产性实训基地</td>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #ffffff;">建设通信技术</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #ffffff;">四川省重点建设专业</td>
                        <td style="padding: 10px; border: 1px solid #ccc; background-color: #f2f2f2;">光纤通信<br>移动通信技术<br>市场营销</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="student" style="transition: transform 0.3s ease; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
        <div class="info" style="padding: 20px; background-color: #f9f9f9; border-radius: 10px; opacity: 0; animation: fadeIn 1s forwards;">
            <h2>全国高校物理实验大赛</h2>
            <p>2022年，我校在全国高校物理实验大赛中表现非常优异，共获得一等奖1项，二等奖2项。这些奖项不仅是对学生实验动手能力的肯定，也为学校的实验教学注入了新的活力，鼓励更多同学积极参与科学实验和研究活动。</p>
        </div>
    </div>

    <div class="student" style="transition: transform 0.3s ease; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
        <div class="info" style="padding: 20px; background-color: #f9f9f9; border-radius: 10px; opacity: 0; animation: fadeIn 1s forwards;">
            <h2>全国青少年科技创新大赛</h2>
            <p>在2023年，全国青少年科技创新大赛中，我校学生凭借其独特的科技创意和严谨的研究方法，获得特等奖1项。此项荣誉不仅鼓励了学生们对科学探索的热情，也促使他们在未来的学习和研究中继续发扬创新精神，努力追求更高的成就。</p>
        </div>
    </div>

    <div class="student" style="transition: transform 0.3s ease; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
        <div class="info" style="padding: 20px; background-color: #f9f9f9; border-radius: 10px; opacity: 0; animation: fadeIn 1s forwards;">
            <h2>全国大学生数学建模竞赛</h2>
            <p>在2023年的全国大学生数学建模竞赛中，我校团队通过严谨的思维和出色的模型构建能力，获得了省级一等奖和全国三等奖的优异成绩。这一成果充分体现了学生们扎实的数学基础和团队协作能力，是他们对数学建模深刻理解的体现。</p>
        </div>
    </div>

    <div class="student" style="transition: transform 0.3s ease; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
        <div class="info" style="padding: 20px; background-color: #f9f9f9; border-radius: 10px; opacity: 0; animation: fadeIn 1s forwards;">
            <h2>全国职业院校技能大赛</h2>
            <p>2020年，我校学生在全国职业院校技能大赛中荣获了多项奖项，包括“移动应用开发大赛”三等奖1项，以及在“网络系统管理大赛”中也获得了三等奖。这些获奖不仅展示了学生们的专业水平，还激励他们在未来的学习中继续追求卓越和创新。</p>
        </div>
    </div>
    `;
    // 重新添加点击事件
    const items = document.querySelectorAll('.dao_');
    items.forEach(item => {
        item.addEventListener('click', function() {
            // 移除所有已选中状态
            items.forEach(i => i.classList.remove('selected'));
            // 为当前点击的元素添加选中状态
            this.classList.add('selected');
        });
    });
    window.scrollTo(0, 0);
}