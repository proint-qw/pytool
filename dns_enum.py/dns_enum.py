import dns.resolver

target_domain = 'youtube.com'
# 移除 CNAME 查询（顶级域名通常无 CNAME 记录）
record_types = ['A', 'AAAA', 'MX', 'TXT', 'SOA']

# 指定可靠的 DNS 服务器（如 Google DNS）
resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8']

for record_type in record_types:
    try:
        answer = resolver.resolve(target_domain, record_type)
        print(f"\n{record_type} records for {target_domain}:")
        for data in answer:
            print(f"  {data}")
    except dns.resolver.NoAnswer:
        # 无记录时跳过
        continue
    except dns.resolver.NXDOMAIN:
        print(f"域名 {target_domain} 不存在")
        break
    except dns.resolver.NoNameservers:
        print(f"查询 {record_type} 记录失败：DNS服务器无响应")
    except Exception as e:
        print(f"查询 {record_type} 记录时发生未知错误：{e}")


    