import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
youtube = [12, 15, 14, 18, 16, 20]
instagram = [8, 9, 11, 10, 12, 13]
spotify = [4, 5, 5, 6, 4, 7]
whatsapp = [3, 4, 3, 5, 4, 6]

fig, axs = plt.subplots(2, 2, figsize=(10, 7), sharex=True)

axs[0, 0].plot(months, youtube, marker='o', color='red')
axs[0, 0].set_title('YouTube')
axs[0, 0].set_ylabel('Data Usage (GB)')

axs[0, 1].plot(months, instagram, marker='o', color='purple')
axs[0, 1].set_title('Instagram')

axs[1, 0].plot(months, spotify, marker='o', color='green')
axs[1, 0].set_title('Spotify')
axs[1, 0].set_xlabel('Months')
axs[1, 0].set_ylabel('Data Usage (GB)')

axs[1, 1].plot(months, whatsapp, marker='o', color='teal')
axs[1, 1].set_title('WhatsApp')
axs[1, 1].set_xlabel('Months')

fig.suptitle('Monthly Mobile Data Usage')
plt.tight_layout()
plt.show()