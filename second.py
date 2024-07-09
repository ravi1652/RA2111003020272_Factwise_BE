# In one step, you can take one card from the beginning or from the end of the row. 
# You have to take exactly k cards.
 
# Your score is the sum of the points of the cards you have taken.
 
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
 
# Example 1:
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
 
# Example 2:
# Input: cardPoints = [2,2,2], k = 2
# Output: 4
 
# Example 3:
# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55


def maxScore(card,k):
    present_sum=sum(card[:k])
    max_sum=present_sum
    
    for i in range(1,k+1):
        present_sum=present_sum-card[k-i]+card[-i]
        max_sum=max(max_sum,present_sum)
    return max_sum
card1=[1,2,3,4,5,6,1]
k1=3
print(maxScore(card1,k1))
card2=[2,2,2]
k2=2
print(maxScore(card2,k2))
card3=[9,7,7,9,7,7,9]
k3=7
print(maxScore(card3,k3))

