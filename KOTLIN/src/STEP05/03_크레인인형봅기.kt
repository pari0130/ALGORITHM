package STEP05

import java.util.*


// https://cote.inflearn.com/contest/10/problem/05-03
// 크레인 인형이 같을 경우 제거 후 스택에서 사라진 개수 출력
/*
in
5
0 0 0 0 0
0 0 1 0 3
0 2 5 0 1
4 2 4 4 2
3 5 1 3 1
8
1 5 3 5 1 2 1 4

out
4
*/

private fun solution(board: Array<IntArray>, moves: IntArray): Int {
    var answer = 0
    val stack = Stack<Int>()
    for (pos in moves) {
        for (i in board.indices) {
            if (board[i][pos - 1] != 0) {
                val tmp = board[i][pos - 1]
                board[i][pos - 1] = 0
                if (!stack.isEmpty() && tmp == stack.peek()) {
                    answer += 2
                    stack.pop()
                } else stack.push(tmp)
                break
            }
        }
    }
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()
    val board = Array(n) { IntArray(n) }
    for (i in 0 until n) {
        for (j in 0 until n) {
            board[i][j] = kb.nextInt()
        }
    }
    val m = kb.nextInt()
    val moves = IntArray(m)
    for (i in 0 until m) moves[i] = kb.nextInt()
    println(solution(board, moves))
}