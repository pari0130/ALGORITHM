package STEP02

import java.lang.StringBuilder
import java.util.Scanner

// 리스트를 입력받아서 리스트의 현재 숫자가 바로 앞의 숫자보다 큰 경우 list 에 담아서 return
// 6
// 7 3 9 5 6 12 >> 7 9 6 12
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val n = kb.nextInt()
    val arr = IntArray(n)

    for(i in 0 until n){
        arr[i] = kb.nextInt()
    }

    for(x in solution(n, arr)){
        print("$x ")
    }
}

private fun solution(n : Int, arr: IntArray): ArrayList<Int> {
    val answer = ArrayList<Int>()
    answer.add(arr[0])

    for(i in 1 until n){
        if(arr[i] > arr[i-1])
            answer.add(arr[i])
    }

    return answer
}