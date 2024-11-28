const items = document.querySelectorAll('.dao_'); // 获取所有的dao_元素

items.forEach(item => {
    item.addEventListener('click', function() {
        // 移除所有已选中状态
        items.forEach(i => i.classList.remove('selected'));
        
        // 为当前点击的元素添加选中状态
        this.classList.add('selected');
    });
});

const shell = document.querySelector('.shell');
const content = document.querySelector('.content');

function updateMargin() {
    const navWidth = shell.offsetWidth + 10; // 获取导航栏当前宽度
    content.style.marginLeft = `${navWidth}px`; // 更新内容的左边距
}

// 页面加载后初始设置
updateMargin();

// 在窗口调整大小时更新
window.addEventListener('resize', updateMargin);
setInterval(updateMargin, 100); // 每100毫秒调用一次