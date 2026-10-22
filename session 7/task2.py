import matplotlib.pyplot as plt

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
posts = [12, 18, 15, 22]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(quarters, posts, marker='o', color='purple')
axs[0, 0].set_title('Line Chart')

axs[0, 1].bar(quarters, posts, color='orange')
axs[0, 1].set_title('Bar Chart')

axs[1, 0].scatter(quarters, posts, color='red', s=80)
axs[1, 0].set_title('Scatter Plot')

axs[1, 1].pie(posts, labels=quarters, autopct='%1.1f%%')
axs[1, 1].set_title('Pie Chart')

fig.suptitle('Instagram Posts per Quarter')
plt.tight_layout()
plt.show()