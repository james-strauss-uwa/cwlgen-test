import cwlgen

cwl_tool = cwlgen.CommandLineTool(tool_id='grep', label='print lines matching a pattern', base_command='grep', cwl_version='v1.0')

file_binding = cwlgen.CommandLineBinding(position=2)
input_file = cwlgen.CommandInputParameter('input_file', param_type='File', input_binding=file_binding, doc='input file from which you want to look for the pattern')
cwl_tool.inputs.append(input_file)

pattern_binding = cwlgen.CommandLineBinding(position=1)
pattern = cwlgen.CommandInputParameter('pattern', param_type='string', input_binding=pattern_binding, doc='pattern to find in the input file')
cwl_tool.inputs.append(pattern)

cwl_tool.export()
