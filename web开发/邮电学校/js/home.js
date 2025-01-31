function home(){
    let doc = document.getElementById("content");
    doc.innerHTML = `
        <header>
            <h1>四川邮电职业技术学院</h1>
        </header>
        
        <div class="carousel">
            <div class="carousel-images">
                <img src="./png/home4.jpg" alt="Image 4">
                <img src="./png/home3.jpg" alt="Image 3">
                <img src="./png/home2.png" alt="Image 2">
                <img src="./png/home1.jpg" alt="Image 1">
            </div>
            <button class="prev" onclick="moveSlide(-1)">&#10094;</button>
            <button class="next" onclick="moveSlide(1)">&#10095;</button>
        </div>
        
        <section>
            <h2>学院概况</h2>
            <p>四川邮电职业技术学院创办于1952年，是中国西南地区一所重要的高等职业技术学院。学院位于四川省成都市，校园环境优美，交通便利，致力于培养高素质、应用型的技术人才。</p>
            <p>学院设置多个专业，涵盖电子与信息技术、计算机软件、网络工程等多个领域，以满足社会对技术人才的需求。</p>
        </section>
        
        <section>
            <h2>办学理念</h2>
            <p>四川邮电职业技术学院始终坚持“以服务为宗旨，以就业为导向”的办学理念，注重培养学生的实践动手能力和创新思维。在课程设计上，学院积极根据行业需求调整教学内容，以确保学生所学知识能够及时与市场接轨。</p>
            <p>学院还加强了对教师队伍的建设，努力提升教师的教育教学水平，鼓励教师参与实际项目，提升其实践能力和教学水平。</p>
        </section>
        
        <section>
            <h2>专业设置</h2>
            <p>学院目前开设的专业包括但不限于：</p>
            <ul>
                <li>电子信息工程技术</li>
                <li>计算机应用技术</li>
                <li>网络工程</li>
                <li>移动通信技术</li>
                <li>云计算技术应用</li>
                <li>软件技术</li>
            </ul>
            <p>每个专业都设置了相应的实训课程，学生通过动手实践，能够更好地掌握所学知识。</p>
        </section>
        
        <section>
            <h2>师资力量</h2>
            <p>学院拥有一支高水平的教师团队，部分教师具有海外留学背景和丰富的企业工作经验。教师不仅承担教学任务，还积极参与科研项目，推动教学和科研相结合的进程。</p>
            <p>学院定期邀请行业专家和知名企业的技术人员来校讲课，开办各类讲座和培训，帮助学生拓宽视野，了解行业发展动态。</p>
        </section>
        
        <section>
            <h2>校园文化</h2>
            <p>四川邮电职业技术学院注重校园文化建设，鼓励学生积极参与各类文体活动。学院每年举办文化节、科技节、运动会等丰富多彩的活动，为学生提供展示自我、锻炼能力的机会。</p>
            <p>此外，学院还设有各种学生社团，丰富学生的课外生活，培养学生的团队合作精神和组织能力。</p>
        </section>
        
        <section>
            <h2>学生就业</h2>
            <p>学院与多家国内外知名企业建立了紧密的合作关系，定期为学生提供实习及就业机会。通过校企合作，学生在校期间能够获得实践机会，提高实际操作能力。</p>
            <p>此外，学院每年举办就业双选会，帮助毕业生与企业进行面对面的交流，为每个学生提供更广阔的就业平台。</p>
        </section>
        
        <section>
            <h2>科研与创新</h2>
            <p>四川邮电职业技术学院在科研方面也取得了不俗的成绩。学院设有多个科研机构和实验室，积极开展应用研究，服务地方经济和社会发展。</p>
            <p>学院鼓励学生参与科研项目，培养学生的创新意识和实践能力。通过项目实践，学生能将所学知识应用于实际，提升综合素质。</p>
        </section>
    `;
    let docc = document.getElementById("sidebar");
    docc.innerHTML = `
    <h3 id="dao" onclick="home()">
        <i class="iconfont icon-daohang_daohanglan_zhuye" id="dao"></i>
        导航栏
    </h3>
    <h2 class='dao_' onclick="jj()"><i class="iconfont icon-01" id="dao"></i>&nbsp;&nbsp;学校简介</h2>
    <h2 class='dao_' onclick="zy()"><i class="iconfont icon-zhuanye" id="dao"></i>&nbsp;&nbsp;学校专业</h2>
    <h2 class='dao_' onclick="kj()"><i  style="font-size: 1em;padding-left:4px;" class="iconfont icon-keji"></i>&nbsp;&nbsp;校园科技</h2>
    <h2 class='dao_' onclick="cj()"><i class="iconfont icon-jiangbei" id="dao" style="font-size: 1.0em;line-height: 1.5;padding-left:5px;"></i>&nbsp;&nbsp;学校成就</h2>
    <p style="font-size: 0.8em; color: #999; margin-top: 10px;" class="xiao_dao_">&nbsp;&nbsp;&nbsp;&nbsp;注：点击导航栏可以返回主页</p>
    `;

    // 重新添加点击事件
    const items = docc.querySelectorAll('.dao_');
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
let currentIndex = 0;

function moveSlide(direction) {
    const images = document.querySelectorAll('.carousel-images img');
    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = images.length - 1;
    } else if (currentIndex >= images.length) {
        currentIndex = 0;
    }

    const imageWidth = images[0].clientWidth; // 动态获取当前图片的宽度
    const offset = -currentIndex * imageWidth; // 根据动态宽度计算偏移量
    document.querySelector('.carousel-images').style.transform = 'translateX(' + offset + 'px)';
}

setInterval(() => moveSlide(1), 5000);
