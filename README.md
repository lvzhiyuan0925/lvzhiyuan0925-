**报错原因，及修复：**

1. **UnpicklingError: could not find MARK**
   - **报错原因：** 该错误通常由于`pickle`模块试图加载一个损坏或不完整的二进制文件而引起。在这里，它在加载名为`数据.pkl`的文件时出现。
   - **修复建议：** 在加载`pickle`文件之前，添加条件检查，确保文件存在且不为空。若文件不存在或为空，则避免加载。

   修复代码示例：
   ```python
   try:
       with open('数据.pkl', 'rb') as file:
           list_1 = pickle.load(file)
           host = str(list_1[0])
           port = int(list_1[1])
           password = str(list_1[2])
           s_2.destroy()
           整体()
   except (_pickle.UnpicklingError, FileNotFoundError, EOFError) as error:
       tk.messagebox.showinfo('错误', f'无法加载数据文件：{error}')
   ```

2. **EOFError: Ran out of input**
   - **报错原因：** 此错误是由于尝试从文件中读取更多数据而导致的。在这里，它发生在尝试加载名为`数据.pkl`的文件时，但该文件可能已经读取完毕。
   - **修复建议：** 在加载`pickle`文件之前，添加异常处理，以便在文件读取完毕时进行处理。

   修复代码示例：
   ```python
   try:
       with open('数据.pkl', 'rb') as file:
           list_1 = pickle.load(file)
           host = str(list_1[0])
           port = int(list_1[1])
           password = str(list_1[2])
           s_2.destroy()
           整体()
   except EOFError:
       tk.messagebox.showinfo('错误', '文件已读取完毕，无法继续加载')
   ```

3. **ValueError: invalid literal for int() with base 10: ''**
   - **报错原因：** 此错误是由于尝试将空字符串转换为整数而引起的。在这里，它发生在尝试将`cc_4_`（端口）的值转换为整数时。
   - **修复建议：** 在转换之前，检查该值是否为非空字符串。如果为空字符串，可以设置默认的端口值或要求用户输入有效的端口。

   修复代码示例：
   ```python
   cc_4_ = cc_4.get()
   if cc_4_ == '':
       tk.messagebox.showinfo('警告', '请输入有效的端口')
   else:
       port = int(cc_4_)
   ```

通过以上修复建议，可以更好地处理这些报错情况，并提高软件的稳定性。
