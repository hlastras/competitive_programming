# Not finished yet

defmodule Master do
  use GenServer

  alias Slave

  # API
  def start_link() do
    GenServer.start_link(__MODULE__, nil)
  end

  #Server
  def init(nil) do
    send(self(), :start_child)
    {:ok, []}
  end

  def handle_info(:start_child, children_list) do
    {:ok, slave} = Slave.start_link(self())
    {:noreply,  children_list ++ [slave]}
  end

  def handle_cast({:slave_start, id}, state) do
    {:noreply,  state}
  end

  def handle_cast({:slave_in, id}, state) do
    {:noreply,  state}
  end

  def handle_cast({:slave_dead, id}, state) do
    {:noreply,  state}
  end
end

defmodule Slave do
  use GenServer
  @ip '52.49.91.111'
  @port 2092

  defstruct [
    :socket,
    :server_id,
    :siblings_ids,
    :parent,
    :lines
  ]

  # API
  def start_link(parent) do
    GenServer.start_link(__MODULE__, parent)
  end

  # SERVER
  def init(parent) do
    {:ok, socket} = :gen_tcp.connect(@ip, @port, [:binary, active: false])
    schedule_tick()
    {:ok, %__MODULE__{socket: socket, server_id: nil, siblings_ids: [], parent: parent, lines: [""]}}
  end

  def handle_info(:next_tick, %__MODULE__{socket: socket, lines: lines} = state) do
    {:ok, {line, rest_lines}} = read_line(socket, lines)
    new_state = Map.put(state, :lines, rest_lines)
    IO.inspect(line)
    send(self(), {:process_line, line})
    schedule_tick()
    {:noreply, new_state}
  end

  def handle_info({:process_line, line}, %__MODULE__{socket: socket} = state) do
    if String.ends_with?(line, "} (ROUND FINISHED)") do
      # {:ok, {servers, owner}} = extract_info(line)
      :ok
    end
    {:noreply, state}
  end

  defp schedule_tick() do
    Process.send_after(self(), :next_tick, 5)
  end

  defp read_line(socket, []) do
    read_line(socket, [""])
  end

  defp read_line(socket, [rest | []]) do
    {:ok, data} = :gen_tcp.recv(socket, 0)
    [line | rest_lines] =
    case String.split(data, "\n") do
      ["" | [line | rest_lines]] -> [line | rest_lines]
      [line | rest_lines] -> [line | rest_lines]
    end
    {:ok, {rest <> line, rest_lines}}
  end

  defp read_line(socket, [line | rest_lines]) do
    {:ok, {line, rest_lines}}
  end
end


{:ok, master} = Master.start_link()
IO.inspect({master, self()})
:timer.sleep(10000)
