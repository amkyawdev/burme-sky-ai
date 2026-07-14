import { ref } from 'vue'

export const useAnimation = () => {
  const isConnected = ref(false)
  const showThanking = ref(false)
  const animationMessage = ref('')

  const showConnectionAnimation = () => {
    isConnected.value = true
    animationMessage.value = 'Connected to AI'
    setTimeout(() => {
      isConnected.value = false
    }, 2000)
  }

  const showThankingAnimation = () => {
    showThanking.value = true
    animationMessage.value = 'Thank you for using Burme Sky AI!'
    setTimeout(() => {
      showThanking.value = false
    }, 3000)
  }

  const hideAllAnimations = () => {
    isConnected.value = false
    showThanking.value = false
  }

  return {
    isConnected,
    showThanking,
    animationMessage,
    showConnectionAnimation,
    showThankingAnimation,
    hideAllAnimations
  }
}
