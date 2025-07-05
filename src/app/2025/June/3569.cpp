class Solution {
public:
    static const int MAXN = 100001;
    bool prime[MAXN];

    // Standard Recursive Segment Tree with Lazy Propagation
    struct SegmentTree {
        int n;
        vector<int> tree, lazy;

        SegmentTree(int size) {
            n = size;
            tree.assign(4 * n, 0);
            lazy.assign(4 * n, 0);
        }

        void push(int node, int start, int end) {
            if (lazy[node] != 0) {
                tree[node] += lazy[node];
                if (start != end) {
                    lazy[node * 2] += lazy[node];
                    lazy[node * 2 + 1] += lazy[node];
                }
                lazy[node] = 0;
            }
        }

        void update(int node, int start, int end, int l, int r, int val) {
            push(node, start, end);
            if (r < start || l > end) return;
            if (l <= start && end <= r) {
                lazy[node] += val;
                push(node, start, end);
                return;
            }
            int mid = (start + end) / 2;
            update(node * 2, start, mid, l, r, val);
            update(node * 2 + 1, mid + 1, end, l, r, val);
            tree[node] = max(tree[node * 2], tree[node * 2 + 1]);
        }

        int query(int node, int start, int end, int l, int r) {
            if (r < start || l > end) return 0;
            push(node, start, end);
            if (l <= start && end <= r) {
                return tree[node];
            }
            int mid = (start + end) / 2;
            int leftMax = query(node * 2, start, mid, l, r);
            int rightMax = query(node * 2 + 1, mid + 1, end, l, r);
            return max(leftMax, rightMax);
        }

        // Helper functions to call from outside with 0-based indexing
        void updateRange(int l, int r, int val) {
            update(1, 0, n - 1, l, r, val);
        }

        int queryRange(int l, int r) {
            return query(1, 0, n - 1, l, r);
        }
    };

    void sieve() {
        fill(begin(prime), end(prime), true);
        prime[0] = prime[1] = false;
        for (int i = 2; i * i < MAXN; ++i) {
            if (prime[i]) {
                for (int j = i * i; j < MAXN; j += i) {
                    prime[j] = false;
                }
            }
        }
    }

    void removePrime(int val, int idx, map<int, set<int>>& occ, SegmentTree& seg, int n) {
        auto& indices = occ[val];
        if (indices.size() == 1) {
            seg.updateRange(1, n - 1, -1);
        } else if (idx == *indices.begin()) {
            seg.updateRange(idx + 1, *next(indices.begin()), -1);
        } else if (idx == *indices.rbegin()) {
            seg.updateRange(*prev(indices.end(), 2) + 1, idx, -1);
        }
        indices.erase(idx);
    }

    void insertPrime(int val, int idx, map<int, set<int>>& occ, SegmentTree& seg, int n) {
        auto& indices = occ[val];
        if (indices.empty()) {
            seg.updateRange(1, n - 1, 1);
        } else if (idx < *indices.begin()) {
            seg.updateRange(idx + 1, *indices.begin(), 1);
        } else if (idx > *indices.rbegin()) {
            seg.updateRange(*indices.rbegin() + 1, idx, 1);
        }
        indices.insert(idx);
    }

    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        sieve();

        map<int, set<int>> occ;
        SegmentTree seg(n);

        for (int i = 0; i < n; ++i) {
            if (prime[nums[i]]) {
                insertPrime(nums[i], i, occ, seg, n);
            }
        }

        vector<int> result;
        for (const auto& query : queries) {
            int idx = query[0];
            int val = query[1];
            if (nums[idx] != val) {
                if (prime[nums[idx]]) {
                    removePrime(nums[idx], idx, occ, seg, n);
                }
                nums[idx] = val;
                if (prime[val]) {
                    insertPrime(val, idx, occ, seg, n);
                }
            }
            // Query the max on [1, n-1] range (0-based indexing: [1..n-1])
            result.push_back(seg.queryRange(1, n - 1));
        }
        return result;
    }
};