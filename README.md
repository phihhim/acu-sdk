# acu-sdk


## Core:
### Class Acunetix:
- ** Gọi 1 service:
  - Yêu cầu url tới server Acunetix + Token
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    # service =  <class Acunetix>
  ```
- **create_target(url, description="")**  
  - tạo 1 target 
  - input: url, có thể có description hoặc không
  - output: json | `None`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    target = service.create_target('http://google.com','this is a description')
  ```

- **create_targets(list_target)**
  - tạo nhiều target  
  - input: danh sách target `list_target`
  - output: json | `[]`
  ```python
    list_target = [{"address": 'http://google.com',"description": "ndqk"}, {"address": 'http://google.com',"description": "ndqk2"}]
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    targets = service.create_targets(list_target)
  ```

- **get_target_by_id(target_id)** 
  - lấy 1 target theo id. 
  - input: `target_id`
  - ouput: json | `None`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    target = service.get_target_by_id('123pl15ni3h45b7g8v9')

  ```

- **get_targets_by_ids(list_id)**
  - lấy danh sách target theo danh sách id
  - input: danh sách id `list_id`
  - output: json | `[]`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    targets = service.get_targets_by_ids(['nj124jni5j4b3ugvyut346k', '456jk3bn7hjv1u236b5jk7i548u'])

  ```

- **get_all_targets()**
  - lấy danh sách tất cả các target có trong cơ sở dữ liệu của acunetix.
  - input: 
  - output: set | `[]`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    targets = service.get_all_targets()

  ```

- **delete_targets(list_id)**
  - xóa các target nằm trong danh sách id.
  - input: danh sách id `list_id`
  - output: đối tượng `Response`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    del = service.delete_targets(['356kjnbgfc54h8tf42kl4556'])
  ```

- **create_scan_from_target(target, profile_id=,schedule=)**
  - tạo scan từ target đã tạo trước. 
  - input: đối tượng `Target`, `profile_id` và `schedule` (`profile_id`, `schedule` có thể có hoặc không)
  - output: scanid | `None`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    target = service.create_target('http://google.com')
    new_scan = service.create_scan_from_target(target)
  ```

- **get_all_scans()**
  - lấy tất cả các scans có trong cơ sở dữ liệu Acunetix. 
  - input: 
  - output: danh sách đối tượng `Scan` | `[]`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    all_scan = service.get_all_scans()
  ```
  
- **get_scan_by_id(id)**
  - lấy scan theo id cho trước. 
  - input: id của scan
  - output: đối tượng `Scan` | `None`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    scan = service.get_scan_by_id('93428622uhjnv5h354')

  ```
   
- **get_scans_by_ids(list_id)**
  - lấy danh sách scan theo danh sách id cho trước. 
  - input: danh sách scan id
  - output: danh sách đối tượng `Scan` | `[]` 
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    scans = service.get_scans_by_ids(['456mlnkj3bn83hjk557c', '0tg8r5k34liuy96787df5667ef'])
  ```

- **pause_scan(scan)**
  - tạm dừng 1 scan. 
  - input: là 1 đối tượng `Scan`.  
  - input: đối tượng `Response`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    scan = service.get_scan_by_id('abc')
    service.pause_scan(scan)
  ```
  
- **resume_scan(scan)**
  - khởi động lại 1 scan đang tạm dừng. 
  - input: là 1 đối tượng `Scan`.  
  - input: đối tượng `Response`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    scan = service.get_scan_by_id('abc')
    service.pause_scan(scan)
    service.resume_scan(scan)
  ```
  
- **stop_scan(scan)**
  - kết thúc 1 scan. 
  - input: là 1 đối tượng `Scan`.  
  - input: đối tượng `Response`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    scan = service.get_scan_by_id('abc')
    service.stop_scan(scan)
  ```
  
- **delete_scan(scan)**
  - xóa 1 scan. 
  - input: là 1 đối tượng `Scan`.  
  - input: đối tượng `Response`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    scan = service.get_scan_by_id('abc')
    service.delete_scan(scan)
  ```

-   **get_results_of_scan(scan)**
  - lấy danh sách các reulst của 1 scan
  - input: đối tượng `Scan` 
  - output: danh sách các đối tượng `Result` |`[]`
  ```python
    service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
    scan = service.get_scan_by_id('abc')
    results = service.get_results_of_scan(scan)
  ```

- **get_vulns_of_result(result)**
  - lấy danh sách các lỗ hổng của 1 kết quả scan
  - input: đối tượng `Result`
  - output: danh sách các đối tượng `Vulnerability` | []
  ```python
     service = Acunetix('127.0.0.1','9238BN45BOKJ12B36H45755B4J13587DFBF')
     scan = service.get_scan_by_id('abc')
     results = service.get_results_of_scan(scan)
     result = results[0]
     vulns = service.get_vulns_of_result(result)
  ```
- **get_result_statistic(result)**
  - lấy dữ liệu thống kê của result (dùng cho biểu diễn quá trình scan)
  - input: đối tượng `Result`
  - output: json ([result](https://github.com/ngdquockhanh/acunetix-sdk/blob/main/statistic.json))
  ```python
    results = Acunetix.get_results_of_scan(scan)
    result = results[0]
    statistic = Acunetix.get_result_statistic(result)
  ```
 
- **get_root_location(result)**
  - lấy thư mục gốc của trang web được scan
  - input: đối tượng `Result`
  - output: đối tượng `Location` | `None`
  ```python
     scan = Acunetix.get_scan_by_id('abc')
     results = Acunetix.get_results_of_scan(scan)
     result = results[0]
     root = Acunetix.get_root_location(result)
  ```


