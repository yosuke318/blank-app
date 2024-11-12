import streamlit as st
import pandas as pd

# サンプルデータの作成
data = pd.DataFrame({
    'ID': range(1, 101),
    'Name': [f'Person {i}' for i in range(1, 101)],
    'Age': [20 + i % 50 for i in range(1, 101)]
})

# タイトルの設定
st.title('レコード表示画面')

# 1ページあたりのレコード数
records_per_page = 10

# 総ページ数の計算
total_pages = len(data) // records_per_page + (1 if len(data) % records_per_page > 0 else 0)

# 現在のページ番号（デフォルトは1）
page_number = st.number_input('ページ番号', min_value=1, max_value=total_pages, value=1)

# 表示するレコードの取得
start_idx = (page_number - 1) * records_per_page
end_idx = start_idx + records_per_page
page_data = data.iloc[start_idx:end_idx]

# データの表示
st.dataframe(page_data)

# ページ情報の表示
st.write(f'ページ {page_number} / {total_pages}')


col1, col2, col3 = st.columns(3)

with col1:
    if st.button('前のページ') and page_number > 1:
        page_number -= 1

with col2:
    st.write(f'ページ {page_number} / {total_pages}')

with col3:
    if st.button('次のページ') and page_number < total_pages:
        page_number += 1